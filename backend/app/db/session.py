# --------------------------------------------------
# File: session.py
# Purpose: Database Engine configuration and SQLModel metadata initialization (SQLite / PostgreSQL).
# Module: Core Database Infrastructure
# Used By: FastAPI Dependencies & Application Lifespan
# --------------------------------------------------

from typing import Generator
from sqlmodel import create_engine, Session, SQLModel
from backend.app.core.config.settings import settings

# Import models package index so SQLModel registers all table metadata
import backend.app.models  # noqa: F401

db_url = settings.DATABASE_URL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if "sqlite" in db_url else {}

engine = create_engine(
    db_url,
    echo=False,
    connect_args=connect_args,
)


def init_db() -> None:
    """Initializes database tables defined across SQLModel entities."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database session."""
    with Session(engine) as session:
        yield session
