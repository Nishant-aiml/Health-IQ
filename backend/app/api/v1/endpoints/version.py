# --------------------------------------------------
# File: version.py
# Purpose: Returns application and API version metadata.
# Module: API Engine / Core System
# Used By: Frontend Navbar, System Info Page
# Future Phase: Phase 1 Foundation
# --------------------------------------------------

from fastapi import APIRouter, Depends
from backend.app.api.dependencies import get_health_service
from backend.app.schemas.base import BaseResponse
from backend.app.schemas.version import VersionInfo
from backend.app.services.health_service import HealthService

router = APIRouter()


@router.get("/version", response_model=BaseResponse[VersionInfo], summary="Version Information")
async def version_info(
    system_health_service: HealthService = Depends(get_health_service),
) -> BaseResponse[VersionInfo]:
    """
    Returns platform application version, API version namespace, and architecture phase.

    Why:
        Provides runtime metadata to frontend UI and client applications.

    Input:
        system_health_service: Injected health service instance.

    Returns:
        BaseResponse containing VersionInfo payload.
    """
    application_version_metadata = system_health_service.get_version()
    return BaseResponse(success=True, data=application_version_metadata, message="Version info retrieved")
