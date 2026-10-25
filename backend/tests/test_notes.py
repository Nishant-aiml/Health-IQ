# --------------------------------------------------
# File: test_notes.py
# Purpose: Unit tests for Clinical Notes service and persistence.
# Module: Backend Test Suite / Clinical Notes
# Used By: Pytest Execution
# Future Phase: Phase 4 Validation
# --------------------------------------------------

from sqlmodel import Session
from backend.app.db.session import engine, init_db
from backend.app.notes.service import clinical_note_service
from backend.app.notes.models import ClinicalNoteCreate, NoteType


def test_clinical_note_creation_and_retrieval():
    init_db()
    with Session(engine) as session:
        note_in = ClinicalNoteCreate(
            report_id=1,
            user_id=1,
            author_name="Dr. Smith",
            author_role="Primary Doctor",
            note_type=NoteType.CLINICAL_OBSERVATION,
            content="Patient demonstrates good glycemic response after dietary adjustment.",
        )
        res = clinical_note_service.add_note(session, note_in)

        assert res.id is not None
        assert res.author_name == "Dr. Smith"

        notes = clinical_note_service.get_notes(session, 1)
        assert len(notes) >= 1
        assert any(n.author_name == "Dr. Smith" for n in notes)
