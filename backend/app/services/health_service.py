from datetime import datetime, timezone
from sqlmodel import Session, select
from backend.app.core.config import settings
from backend.app.schemas.health import HealthStatus
from backend.app.schemas.version import VersionInfo
from backend.app.services.base import BaseService


class HealthService(BaseService):
    def get_health(self, session: Session) -> HealthStatus:
        db_status = "connected"
        try:
            # Simple ping to test DB connectivity
            session.exec(select(1)).first()
        except Exception:
            db_status = "disconnected"

        return HealthStatus(
            status="healthy" if db_status == "connected" else "degraded",
            database=db_status,
            environment=settings.APP_ENV,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def get_version(self) -> VersionInfo:
        return VersionInfo(
            name=settings.APP_NAME,
            version=settings.APP_VERSION,
            api_version=settings.API_V1_STR,
            architecture_phase="Phase 1 - Project Foundation",
        )


health_service = HealthService()
