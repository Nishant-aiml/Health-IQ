# --------------------------------------------------
# File: notes.py
# Purpose: Clinical Notes API endpoints (POST /notes, GET /notes).
# Module: API Engine / Endpoints
# Used By: Frontend NotesPanel Component
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Optional
from fastapi import APIRouter, Depends, Query, Body
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.notes.service import clinical_note_service
from backend.app.notes.models import ClinicalNoteCreate
from backend.app.schemas.base import BaseResponse

router = APIRouter(prefix="/notes", tags=["Clinical Notes Engine"])


@router.post("", summary="Add Timestamped Clinical Note")
async def create_note_endpoint(
    note_in: ClinicalNoteCreate = Body(...),
    db_session: Session = Depends(get_db_session),
):
    """Adds a timestamped clinical observation, visit summary, patient question, or doctor comment."""
    data = clinical_note_service.add_note(db_session, note_in)
    return BaseResponse(success=True, data=data.model_dump(), message="Clinical note saved successfully.")


@router.get("", summary="Get Clinical Notes for Report")
async def get_notes_endpoint(
    report_id: int = Query(1),
    db_session: Session = Depends(get_db_session),
):
    """Retrieves all clinical observations and notes associated with a specific report."""
    data = clinical_note_service.get_notes(db_session, report_id)
    return BaseResponse(success=True, data=[n.model_dump() for n in data], message="Clinical notes retrieved.")
