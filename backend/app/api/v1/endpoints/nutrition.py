# --------------------------------------------------
# File: nutrition.py
# Purpose: Nutrition API Endpoints (/nutrition/{report_id}).
# Module: API Engine / Endpoints
# Used By: Frontend Nutrition Dashboard & Components
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.nutrition_service import nutrition_service
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/nutrition", tags=["Nutrition & Lifestyle Intelligence Engine"])


@router.get("/{report_id}", summary="Get Nutrition Guidance & Food-Drug Interactions")
async def get_nutrition_guidance_endpoint(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches evidence-backed food guidance, food-drug interaction warnings, and circadian meal timing."""
    data = nutrition_service.get_nutrition_guidance_for_report(db_session, report_id)
    return BaseResponse(success=True, data=data, message="Nutrition guidance retrieved.")
