# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Clinical Notes Engine.
# Module: Clinical Notes Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.notes.service import clinical_note_service, ClinicalNoteService
from backend.app.notes.repository import clinical_note_repository, ClinicalNoteRepository


class NotesRegistry:
    def get_service(self) -> ClinicalNoteService:
        return clinical_note_service

    def get_repository(self) -> ClinicalNoteRepository:
        return clinical_note_repository


notes_registry = NotesRegistry()
