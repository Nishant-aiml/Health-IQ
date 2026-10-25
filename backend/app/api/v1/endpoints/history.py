# --------------------------------------------------
# File: history.py
# Purpose: History API Endpoints (/history/{user_id}, /timeline, /trends, /compare).
# Module: API Engine / Endpoints
# Used By: Frontend History Dashboard & Components
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from fastapi import APIRouter, Depends, Query, Body
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.history_service import history_service
from backend.app.history.change.models import ComparisonMode
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/history", tags=["Longitudinal Health Intelligence Engine"])


@router.get("/{user_id}", summary="Get Patient Report History & Health Score Evolution")
async def get_patient_history_endpoint(
    user_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches all historical reports, collection dates, and health score trajectory."""
    data = history_service.get_patient_history(db_session, user_id)
    return BaseResponse(success=True, data=data, message="Patient history retrieved.")


@router.get("/{user_id}/timeline", summary="Get Patient Health Journey Timeline")
async def get_patient_timeline_endpoint(
    user_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches chronological patient timeline events (Uploads, Score Changes, Alerts)."""
    data = history_service.get_patient_timeline(db_session, user_id)
    return BaseResponse(success=True, data=data, message="Patient timeline retrieved.")


@router.get("/{user_id}/trends", summary="Get Biomarker Trends & Time-Series Analytics")
async def get_patient_trends_endpoint(
    user_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches biomarker trend classifications, statistics, and extended recommendations."""
    data = history_service.get_patient_trends(db_session, user_id)
    return BaseResponse(success=True, data=data, message="Biomarker trends retrieved.")


@router.get("/{user_id}/compare", summary="Compare Current vs Reference Report")
async def compare_reports_get_endpoint(
    user_id: int,
    target_report_id: int = Query(...),
    reference_report_id: int = Query(...),
    mode: ComparisonMode = Query(ComparisonMode.PREVIOUS),
    db_session: Session = Depends(get_db_session),
):
    """Compares two report IDs across comparison modes (PREVIOUS, BASELINE, BEST, CUSTOM_RANGE)."""
    data = history_service.compare_reports_by_ids(
        db_session,
        mode=mode,
        target_report_id=target_report_id,
        reference_report_id=reference_report_id,
    )
    return BaseResponse(success=True, data=data, message="Report comparison retrieved.")


@router.post("/compare", summary="Post Report Comparison Request")
async def compare_reports_post_endpoint(
    payload: dict = Body(...),
    db_session: Session = Depends(get_db_session),
):
    """Post endpoint for comparing any two specified report IDs."""
    target_id = int(payload.get("target_report_id", 1))
    reference_id = int(payload.get("reference_report_id", 1))
    mode_str = payload.get("mode", "PREVIOUS")
    mode = ComparisonMode(mode_str)

    data = history_service.compare_reports_by_ids(
        db_session,
        mode=mode,
        target_report_id=target_id,
        reference_report_id=reference_id,
    )
    return BaseResponse(success=True, data=data, message="Report comparison retrieved.")
