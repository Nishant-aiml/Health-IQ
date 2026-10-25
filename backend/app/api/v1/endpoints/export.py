# --------------------------------------------------
# File: export.py
# Purpose: Export API Endpoints (PDF, JSON, CSV).
# Module: API Engine / Endpoints
# Used By: Frontend QuickActions Toolbar & Export Modals
# Future Phase: Phase 2E Export System
# --------------------------------------------------

from fastapi import APIRouter, Depends, Response
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.report_service import report_service
from backend.app.services.recommendation_service import recommendation_service
from backend.app.export.pdf_export import pdf_export_service
from backend.app.export.json_export import json_export_service
from backend.app.export.csv_export import csv_export_service

router = APIRouter(prefix="/reports", tags=["Export Engine"])


@router.get("/{report_id}/pdf", summary="Download Professional PDF Medical Report")
async def download_report_pdf(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Generates and downloads a hospital-quality ReportLab PDF medical report."""
    analysis = report_service.get_report_analysis(db_session, report_id)
    bundle = recommendation_service.get_recommendations_for_report(db_session, report_id).dict()
    pdf_bytes = pdf_export_service.generate_pdf_bytes(analysis, bundle)

    filename = f"HealthLens_Medical_Report_{report_id}.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/{report_id}/json", summary="Download Versioned JSON Medical Report")
async def download_report_json(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Generates and downloads a versioned JSON representation (schema 1.0) of the report analysis."""
    analysis = report_service.get_report_analysis(db_session, report_id)
    bundle = recommendation_service.get_recommendations_for_report(db_session, report_id).dict()
    json_str = json_export_service.generate_json_export(analysis, bundle)

    filename = f"HealthLens_Medical_Report_{report_id}.json"
    return Response(
        content=json_str,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/{report_id}/csv", summary="Download Multi-Dataset CSV Medical Report")
async def download_report_csv(
    report_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Generates and downloads a CSV export containing parameters, recommendations, and alerts."""
    analysis = report_service.get_report_analysis(db_session, report_id)
    bundle = recommendation_service.get_recommendations_for_report(db_session, report_id).dict()
    csv_str = csv_export_service.generate_csv_export(analysis, bundle)

    filename = f"HealthLens_Medical_Report_{report_id}.csv"
    return Response(
        content=csv_str,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
