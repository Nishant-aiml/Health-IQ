# --------------------------------------------------
# File: session.py
# Purpose: Database Engine configuration and SQLModel metadata initialization (SQLite / PostgreSQL).
# Module: Core Database Infrastructure
# Used By: FastAPI Dependencies & Application Lifespan
# --------------------------------------------------

import time
from typing import Generator
from sqlmodel import create_engine, Session, SQLModel
from backend.app.core.config.settings import settings
from backend.app.core.logging import logger

# Import models package index so SQLModel registers all table metadata
import backend.app.models  # noqa: F401


def get_normalized_db_url(url: str) -> str:
    """
    Normalizes database URLs for SQLAlchemy 2.0 / 2.1 and cloud providers like Render.
    Explicitly specifies the psycopg2 driver to eliminate dialect ambiguity across Python versions.
    """
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif url.startswith("postgresql://") and "+" not in url.split("://")[0]:
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url


db_url = get_normalized_db_url(settings.DATABASE_URL)

connect_args = {}
engine_kwargs = {"echo": False}

if "sqlite" in db_url:
    connect_args["check_same_thread"] = False
else:
    # PostgreSQL production tuning
    connect_args["connect_timeout"] = 10
    engine_kwargs["pool_pre_ping"] = True
    engine_kwargs["pool_recycle"] = 300

engine = create_engine(
    db_url,
    connect_args=connect_args,
    **engine_kwargs,
)


def _mask_url(raw_url: str) -> str:
    """Masks credentials in database URL for safe logging."""
    if "@" in raw_url:
        try:
            prefix = raw_url.split("://")[0]
            host_part = raw_url.split("@")[-1]
            return f"{prefix}://*****@{host_part}"
        except Exception:
            return "postgresql://*****"
    return raw_url


def init_db(max_retries: int = 5, retry_delay: float = 3.0) -> None:
    """
    Initializes database tables defined across SQLModel entities.
    Includes connection retry logic for cloud-hosted databases (e.g. Render PostgreSQL)
    that may experience brief cold-start or provisioning delays.
    """
    global engine
    safe_target = _mask_url(db_url)
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Connecting to database [attempt {attempt}/{max_retries}] at {safe_target}...")
            SQLModel.metadata.create_all(engine)
            logger.info("Database connection verified and schemas initialized successfully.")
            # Seed baseline patient dataset if database is empty
            try:
                from backend.app.db.seed import seed_database_if_empty
                with Session(engine) as seed_session:
                    seed_database_if_empty(seed_session)
            except Exception as seed_err:
                logger.warning(f"Seed initialization note: {seed_err}")
            return
        except Exception as exc:
            last_exception = exc
            logger.warning(f"Database connection attempt {attempt}/{max_retries} failed: {exc}")
            if attempt < max_retries:
                logger.info(f"Retrying database connection in {retry_delay:.1f}s...")
                time.sleep(retry_delay)

    # Check if fallback to SQLite is allowed
    if settings.DB_FALLBACK_TO_SQLITE:
        logger.error(
            f"PostgreSQL connection to {safe_target} failed after {max_retries} attempts. "
            "Falling back to local SQLite as configured by DB_FALLBACK_TO_SQLITE."
        )
        fallback_url = "sqlite:///./health_companion.db"
        engine = create_engine(
            fallback_url,
            echo=False,
            connect_args={"check_same_thread": False},
        )
        SQLModel.metadata.create_all(engine)
        logger.warning("Initialized fallback SQLite database schemas successfully.")
        try:
            from backend.app.db.seed import seed_database_if_empty
            with Session(engine) as seed_session:
                seed_database_if_empty(seed_session)
        except Exception as seed_err:
            logger.warning(f"Seed initialization note: {seed_err}")
        return

    # Otherwise raise error with actionable troubleshooting details
    logger.error(
        "========================================================================\n"
        f"DATABASE CONNECTION FAILURE: Unable to connect to {safe_target}\n"
        f"Error: {last_exception}\n\n"
        "Render Troubleshooting Checklist:\n"
        "1. REGION MISMATCH: If your PostgreSQL database and Web Service are in different\n"
        "   Render regions, the 'Internal Database URL' will NOT resolve. You must use the\n"
        "   'External Database URL' instead.\n"
        "2. PROVISIONING DELAY: If the database was just created, wait ~60s for Render to finish\n"
        "   provisioning and trigger 'Manual Deploy' -> 'Clear build cache & deploy'.\n"
        "3. DATABASE CREDENTIALS: Verify DATABASE_URL in Render Dashboard > Environment.\n"
        "========================================================================"
    )
    raise last_exception


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database session."""
    with Session(engine) as session:
        yield session
