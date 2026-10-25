# --------------------------------------------------
# File: health.py
# Purpose: System health check controller endpoint.
# Module: API Engine / Core System
# Used By: Frontend Navbar, System Monitors
# Future Phase: Phase 1 Foundation
# --------------------------------------------------

from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session, get_health_service
from backend.app.schemas.base import BaseResponse
from backend.app.schemas.health import HealthStatus
from backend.app.services.health_service import HealthService

router = APIRouter()


@router.get("/health", response_model=BaseResponse[HealthStatus], summary="Health Check")
async def health_check(
    db_session: Session = Depends(get_db_session),
    system_health_service: HealthService = Depends(get_health_service),
) -> BaseResponse[HealthStatus]:
    """
    Evaluates system operational status and database connectivity.

    Why:
        Allows frontend monitors and health checkers to verify backend health.

    Input:
        db_session: Database session dependency.
        system_health_service: Injected health service instance.

    Returns:
        BaseResponse containing HealthStatus payload.
    """
    health_status_result = system_health_service.get_health(db_session)
    return BaseResponse(success=True, data=health_status_result, message="System operational")
