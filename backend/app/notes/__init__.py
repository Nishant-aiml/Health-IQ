# --------------------------------------------------
# File: __init__.py
# Purpose: Clinical Notes Engine package index.
# Module: Clinical Notes Engine
# Used By: Services & Application
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.notes.models import NoteType, ClinicalNote, ClinicalNoteCreate, ClinicalNoteResponse
from backend.app.notes.repository import ClinicalNoteRepository, clinical_note_repository
from backend.app.notes.service import ClinicalNoteService, clinical_note_service
from backend.app.notes.registry import NotesRegistry, notes_registry

__all__ = [
    "NoteType",
    "ClinicalNote",
    "ClinicalNoteCreate",
    "ClinicalNoteResponse",
    "ClinicalNoteRepository",
    "clinical_note_repository",
    "ClinicalNoteService",
    "clinical_note_service",
    "NotesRegistry",
    "notes_registry",
]
