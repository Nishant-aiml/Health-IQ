# --------------------------------------------------
# File: service.py
# Purpose: Service layer for Clinical Notes handling creation and retrieval.
# Module: Clinical Notes Engine / Service
# Used By: Clinical Notes API Controller
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import List
from sqlmodel import Session
from backend.app.notes.models import ClinicalNote, ClinicalNoteCreate, ClinicalNoteResponse
from backend.app.notes.repository import clinical_note_repository


class ClinicalNoteService:
    """Service layer managing clinical notes."""

    def add_note(self, session: Session, note_in: ClinicalNoteCreate) -> ClinicalNoteResponse:
        note = clinical_note_repository.create_note(session, note_in)
        return ClinicalNoteResponse(
            id=note.id,
            report_id=note.report_id,
            user_id=note.user_id,
            author_name=note.author_name,
            author_role=note.author_role,
            note_type=note.note_type,
            content=note.content,
            created_at=note.created_at.isoformat(),
        )

    def get_notes(self, session: Session, report_id: Optional[int] = None, user_id: Optional[int] = None) -> List[ClinicalNoteResponse]:
        notes = clinical_note_repository.get_notes(session, report_id=report_id, user_id=user_id)
        return [
            ClinicalNoteResponse(
                id=n.id,
                report_id=n.report_id,
                user_id=n.user_id,
                author_name=n.author_name,
                author_role=n.author_role,
                note_type=n.note_type,
                content=n.content,
                created_at=n.created_at.isoformat(),
            )
            for n in notes
        ]


clinical_note_service = ClinicalNoteService()
