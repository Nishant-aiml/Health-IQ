# --------------------------------------------------
# File: prescriptions.py
# Purpose: Prescriptions API Endpoints (/analyze, /{id}, /{id}/medicines).
# Module: API Engine / Endpoints
# Used By: Frontend Prescription Uploader & Dashboard Pages
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.prescription_service import prescription_service
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/prescriptions", tags=["Prescription Intelligence Engine"])


@router.post("/analyze", summary="Analyze Uploaded Prescription or Pasted Text")
async def analyze_prescription_endpoint(
    file: Optional[UploadFile] = File(None),
    pasted_text: Optional[str] = Form(None),
    db_session: Session = Depends(get_db_session),
):
    """
    Submits a prescription image/PDF/DOCX/TXT file or pasted text for complete Medicine Intelligence Analysis.
    """
    file_bytes = None
    filename = "prescription.pdf"

    if file:
        file_bytes = await file.read()
        filename = file.filename

    analysis = await prescription_service.analyze_prescription(
        db_session,
        file_bytes=file_bytes,
        filename=filename,
        pasted_text=pasted_text,
    )

    return BaseResponse(
        success=True,
        data=analysis,
        message="Prescription analysis completed successfully.",
    )


@router.get("/{prescription_id}", summary="Get Prescription Analysis")
async def get_prescription(
    prescription_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches comprehensive prescription analysis by ID."""
    analysis = prescription_service.get_prescription_by_id(db_session, prescription_id)
    return BaseResponse(success=True, data=analysis, message="Prescription analysis retrieved.")


@router.get("/{prescription_id}/medicines", summary="Get Extracted Medicines & Safety Analysis")
async def get_prescription_medicines(
    prescription_id: int,
    db_session: Session = Depends(get_db_session),
):
    """Fetches extracted medicines, data-driven daily schedules, interactions, and RAG evidence citations."""
    analysis = prescription_service.get_prescription_by_id(db_session, prescription_id)
    return BaseResponse(
        success=True,
        data={
            "medicines": analysis["medicines"],
            "safety_analysis": analysis["safety_analysis"],
        },
        message="Medicines retrieved.",
    )
