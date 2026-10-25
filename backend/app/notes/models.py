# --------------------------------------------------
# File: models.py
# Purpose: Domain models & SQLModel database table for Clinical Notes (Observations, Visit Summaries, Patient Questions, Doctor Comments).
# Module: Clinical Notes Engine / Models
# Used By: Notes Repository & Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from datetime import datetime
from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class NoteType(str, Enum):
    CLINICAL_OBSERVATION = "Clinical Observation"
    VISIT_SUMMARY = "Visit Summary"
    PATIENT_QUESTION = "Patient Question"
    DOCTOR_COMMENT = "Doctor Comment"


class ClinicalNote(SQLModel, table=True):
    __tablename__ = "clinical_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(index=True)
    user_id: int = Field(default=1, index=True)
    author_name: str = Field(default="Dr. Physician")
    author_role: str = Field(default="Primary Doctor")
    note_type: NoteType = Field(default=NoteType.CLINICAL_OBSERVATION)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ClinicalNoteCreate(BaseModel):
    report_id: int
    user_id: int = 1
    author_name: str = "Dr. Physician"
    author_role: str = "Primary Doctor"
    note_type: NoteType = NoteType.CLINICAL_OBSERVATION
    content: str


class ClinicalNoteResponse(BaseModel):
    id: int
    report_id: int
    user_id: int
    author_name: str
    author_role: str
    note_type: NoteType
    content: str
    created_at: str
