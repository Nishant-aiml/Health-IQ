from typing import Generator
from fastapi import Depends
from sqlmodel import Session
from backend.app.db.session import get_session
from backend.app.services.health_service import HealthService, health_service


def get_db_session() -> Generator[Session, None, None]:
    """Yields a database session via session factory dependency."""
    yield from get_session()


def get_health_service() -> HealthService:
    """Provides HealthService instance."""
    return health_service
