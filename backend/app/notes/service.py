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
            id=note.id or 1,
            note_id=str(note.id or 1),
            report_id=note.report_id or 1,
            user_id=note.user_id or 1,
            title=note.title or "Clinical Note",
            author_name=note.author_name or "Dr. Physician",
            author_role=note.author_role or "Primary Doctor",
            note_type=note.note_type.value if hasattr(note.note_type, 'value') else str(note.note_type),
            content=note.content,
            created_at=note.created_at.isoformat() if hasattr(note.created_at, 'isoformat') else str(note.created_at),
        )

    def get_notes(self, session: Session, report_id: Optional[int] = None, user_id: Optional[int] = None) -> List[ClinicalNoteResponse]:
        notes = clinical_note_repository.get_notes(session, report_id=report_id, user_id=user_id)
        return [
            ClinicalNoteResponse(
                id=n.id or idx + 1,
                note_id=str(n.id or idx + 1),
                report_id=n.report_id or 1,
                user_id=n.user_id or 1,
                title=n.title or "Clinical Note",
                author_name=n.author_name or "Dr. Physician",
                author_role=n.author_role or "Primary Doctor",
                note_type=n.note_type.value if hasattr(n.note_type, 'value') else str(n.note_type),
                content=n.content,
                created_at=n.created_at.isoformat() if hasattr(n.created_at, 'isoformat') else str(n.created_at),
            )
            for idx, n in enumerate(notes)
        ]


clinical_note_service = ClinicalNoteService()
