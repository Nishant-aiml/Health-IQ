# --------------------------------------------------
# File: prescription_medicine.py
# Purpose: Normalized SQLModel table storing individual prescribed medicine items.
# Module: Core Database Models
# Used By: Prescription Service & Medicine Intelligence Engine
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Optional
from sqlmodel import SQLModel, Field


class PrescriptionMedicine(SQLModel, table=True):
    __tablename__ = "prescription_medicines"

    id: Optional[int] = Field(default=None, primary_key=True)
    prescription_id: int = Field(foreign_key="prescriptions.id", index=True)
    medicine_name_raw: str
    brand_name: Optional[str] = None
    generic_name: str
    active_ingredient: Optional[str] = None
    dosage: str = Field(default="As prescribed")
    frequency_code: str = Field(default="OD", description="OD, BD, TDS, QID, HS, SOS")
    times_per_day: int = Field(default=1)
    timing_slots: str = Field(default="Morning", description="Comma-separated: Morning, Afternoon, Evening, Night")
    relation_to_food: str = Field(default="after_food", description="before_food, after_food, with_food")
    purpose: Optional[str] = None
    drug_class: Optional[str] = None
    category: Optional[str] = None
    ocr_confidence: float = Field(default=1.0)
    resolution_confidence: float = Field(default=1.0)
    knowledge_confidence: float = Field(default=1.0)
