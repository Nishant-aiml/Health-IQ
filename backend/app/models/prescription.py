# --------------------------------------------------
# File: prescription.py
# Purpose: Prescription SQLModel database entity model.
# Module: Core Database Models
# Used By: Prescription Service & Ingestion Pipeline
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Optional
from sqlmodel import SQLModel, Field


class Prescription(SQLModel, table=True):
    __tablename__ = "prescriptions"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    medicine_name_raw: str = Field(default="Multiple Prescribed Medicines")
    generic_name: Optional[str] = Field(default=None)
    active_ingredient: Optional[str] = Field(default=None)
    dosage: str = Field(default="As prescribed")
    frequency: str = Field(default="OD")
    duration: str = Field(default="7 days")
