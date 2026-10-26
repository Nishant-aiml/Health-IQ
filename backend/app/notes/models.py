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
    report_id: Optional[int] = Field(default=1, index=True)
    user_id: int = Field(default=1, index=True)
    title: Optional[str] = Field(default="Clinical Note")
    author_name: str = Field(default="Dr. Physician")
    author_role: str = Field(default="Primary Doctor")
    note_type: NoteType = Field(default=NoteType.CLINICAL_OBSERVATION)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ClinicalNoteCreate(BaseModel):
    report_id: Optional[int] = 1
    user_id: Optional[int] = 1
    title: Optional[str] = "Clinical Note"
    author_name: Optional[str] = "Dr. Physician"
    author_role: Optional[str] = "Primary Doctor"
    note_type: Optional[NoteType] = NoteType.CLINICAL_OBSERVATION
    content: str


class ClinicalNoteResponse(BaseModel):
    id: int
    note_id: Optional[str] = None
    report_id: int
    user_id: int
    title: Optional[str] = "Clinical Note"
    author_name: str
    author_role: str
    note_type: str
    content: str
    created_at: str
    note_type: NoteType
    content: str
    created_at: str
