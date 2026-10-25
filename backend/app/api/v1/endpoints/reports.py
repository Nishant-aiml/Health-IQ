# --------------------------------------------------
# File: reports.py
# Purpose: Reports & Recommendations API Endpoints.
# Module: API Engine / Endpoints
# Used By: Frontend Results Dashboard
# Future Phase: Phase 2B Analysis & Phase 2C Recommendations
# --------------------------------------------------

from typing import Dict, Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.report_service import report_service
from backend.app.services.recommendation_service import recommendation_service
from backend.app.schemas.base import BaseResponse
from backend.app.ai.models import RecommendationBundle

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/{report_id}", response_model=BaseResponse[Dict[str, Any]], summary="Get Report Analysis & Health Score")
async def get_report_by_id(
    report_id: int,
    db_session: Session = Depends(get_db_session),
) -> BaseResponse[Dict[str, Any]]:
    """
    Retrieves full deterministic analysis for a report, including Health Score (0-100),
    severity-tagged parameters, critical alerts, and cross-parameter patterns.
    """
    analysis_data = report_service.get_report_analysis(db_session, report_id)
    return BaseResponse(success=True, data=analysis_data, message="Report analysis fetched successfully.")


@router.get("/{report_id}/recommendations", response_model=BaseResponse[RecommendationBundle], summary="Get Structured AI Recommendations & Health Insights")
async def get_report_recommendations(
    report_id: int,
    db_session: Session = Depends(get_db_session),
) -> BaseResponse[RecommendationBundle]:
    """
    Retrieves structured AI recommendations, evidence reasoning chains, clinical limitations,
    doctor discussion questions, and ELI10 plain-language explanations for a report.

    Why:
        Consumes Phase 2B outputs directly without recomputing health scores or re-running OCR.

    Inputs:
        report_id: Database report ID integer.

    Returns:
        BaseResponse containing RecommendationBundle.
    """
    bundle = recommendation_service.get_recommendations_for_report(db_session, report_id)
    return BaseResponse(success=True, data=bundle, message="Recommendations bundle generated successfully.")
