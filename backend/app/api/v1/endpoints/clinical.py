# --------------------------------------------------
# File: clinical.py
# Purpose: Clinical Collaboration API endpoints (/clinical/package, /clinical/timeline, /clinical/export).
# Module: API Engine / Endpoints
# Used By: Frontend Clinical Summary & Doctor Package Page
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.clinical_service import clinical_service
from backend.app.clinical.models import AudienceTarget
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/clinical", tags=["Clinical Collaboration Engine"])


@router.get("/package", summary="Generate Immutable Clinical Case Package")
async def get_clinical_package_endpoint(
    report_id: int = Query(1),
    user_id: int = Query(1),
    audience: AudienceTarget = Query(AudienceTarget.DOCTOR),
    db_session: Session = Depends(get_db_session),
):
    """Generates an immutable Clinical Case Package with SHA-256 integrity hash, questions for physician, and evidence graph."""
    data = clinical_service.generate_case_package(db_session, report_id, user_id, audience)
    return BaseResponse(success=True, data=data, message="Clinical case package generated successfully.")


@router.get("/timeline", summary="Get Extended Clinical Timeline")
async def get_clinical_timeline_endpoint(
    report_id: int = Query(1),
    user_id: int = Query(1),
    db_session: Session = Depends(get_db_session),
):
    """Retrieves extended clinical timeline uniting report history, doctor notes, and lifestyle milestones."""
    data = clinical_service.get_extended_clinical_timeline(db_session, user_id, report_id)
    return BaseResponse(success=True, data=data, message="Extended clinical timeline retrieved.")


@router.get("/export", summary="Export FHIR R4 Collection Bundle")
async def export_fhir_endpoint(
    report_id: int = Query(1),
    user_id: int = Query(1),
    db_session: Session = Depends(get_db_session),
):
    """Exports structured HL7 FHIR R4 JSON Bundle mapping Patient, DiagnosticReport, and Observation resources."""
    data = clinical_service.export_fhir_bundle(db_session, report_id, user_id)
    return BaseResponse(success=True, data=data, message="FHIR R4 collection bundle exported successfully.")
