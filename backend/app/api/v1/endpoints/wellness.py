# --------------------------------------------------
# File: wellness.py
# Purpose: Wellness API Endpoints (/wellness/{report_id}).
# Module: API Engine / Endpoints
# Used By: Frontend Wellness Score Visualizer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.wellness_service import wellness_service
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/wellness", tags=["Nutrition & Lifestyle Intelligence Engine"])


@router.get("/{report_id}", summary="Get Composite Wellness Score Breakdown")
async def get_wellness_breakdown_endpoint(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches transparent Wellness Score breakdown (Nutrition, Lifestyle, Hydration, Sleep, Overall Score)."""
    data = wellness_service.get_wellness_breakdown_for_report(db_session, report_id)
    return BaseResponse(success=True, data=data, message="Wellness score breakdown retrieved.")
