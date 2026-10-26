# --------------------------------------------------
# File: repository.py
# Purpose: Database repository for Clinical Notes CRUD operations.
# Module: Clinical Notes Engine / Repository
# Used By: Notes Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import List
from sqlmodel import Session, select
from backend.app.notes.models import ClinicalNote, ClinicalNoteCreate


class ClinicalNoteRepository:
    """Repository handling SQLModel persistence for clinical notes."""

    def create_note(self, session: Session, note_in: ClinicalNoteCreate) -> ClinicalNote:
        db_note = ClinicalNote.model_validate(note_in)
        session.add(db_note)
        session.commit()
        session.refresh(db_note)
        return db_note

    def get_notes(self, session: Session, report_id: Optional[int] = None, user_id: Optional[int] = None) -> List[ClinicalNote]:
        statement = select(ClinicalNote)
        if report_id is not None:
            statement = statement.where(ClinicalNote.report_id == report_id)
        elif user_id is not None:
            statement = statement.where(ClinicalNote.user_id == user_id)
        statement = statement.order_by(ClinicalNote.created_at.desc())
        return list(session.exec(statement).all())

    def get_notes_for_report(self, session: Session, report_id: int) -> List[ClinicalNote]:
        return self.get_notes(session, report_id=report_id)


clinical_note_repository = ClinicalNoteRepository()
