# --------------------------------------------------
# File: lifestyle.py
# Purpose: Lifestyle API Endpoints (/lifestyle/{report_id}).
# Module: API Engine / Endpoints
# Used By: Frontend Lifestyle Dashboard & Components
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.lifestyle_service import lifestyle_service
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/lifestyle", tags=["Nutrition & Lifestyle Intelligence Engine"])


@router.get("/{report_id}", summary="Get Lifestyle, Exercise, Sleep & Hydration Plan")
async def get_lifestyle_guidance_endpoint(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches physical activity, sleep hygiene, hydration target, and stress management guidance."""
    data = lifestyle_service.get_lifestyle_guidance_for_report(db_session, report_id)
    return BaseResponse(success=True, data=data, message="Lifestyle guidance retrieved.")
