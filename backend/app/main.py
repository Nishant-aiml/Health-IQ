# --------------------------------------------------
# File: main.py
# Purpose: FastAPI Application Entry Point & Lifespan Hooks.
# Module: Core Infrastructure
# Used By: Server Runners (Uvicorn)
# Future Phase: Phase 1 Foundation & Phase 2A Ingestion
# --------------------------------------------------

from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.app.core.config import settings
from backend.app.core.logging import logger
from backend.app.core.exceptions import (
    AppException,
    app_exception_handler,
    unhandled_exception_handler,
)
from backend.app.core.middleware import RequestTimingAndLoggingMiddleware
from backend.app.core.security import setup_security
from backend.app.db.session import init_db
from backend.app.ingestion.queue import start_worker, stop_worker
from backend.app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    """
    FastAPI Application Lifespan Context Manager.

    What problem it solves:
        Ensures resources (database tables, async ingestion worker loop) are initialized
        before the server accepts HTTP traffic, and guarantees clean cleanup on shutdown.

    Step-by-step logic:
        1. Logs startup notification.
        2. Calls `init_db()` to generate SQLModel database tables.
        3. Calls `start_worker()` to launch background document queue consumer.
        4. Yields control to FastAPI.
        5. On shutdown, calls `stop_worker()`.
    """
    logger.info(f"Starting {settings.APP_NAME} in {settings.APP_ENV} mode...")
    init_db()
    logger.info("Database schemas verified and initialized successfully.")
    start_worker()
    yield
    stop_worker()
    logger.info("Application shutdown completed successfully.")


def create_application() -> FastAPI:
    configured_app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    setup_security(configured_app)
    configured_app.add_middleware(RequestTimingAndLoggingMiddleware)
    configured_app.add_exception_handler(AppException, app_exception_handler)
    configured_app.add_exception_handler(Exception, unhandled_exception_handler)
    configured_app.include_router(api_router, prefix=settings.API_V1_STR)

    return configured_app


app = create_application()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
