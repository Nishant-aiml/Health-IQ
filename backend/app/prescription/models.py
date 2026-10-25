# --------------------------------------------------
# File: models.py
# Purpose: Domain models for raw and structured prescription parse results.
# Module: Prescription OCR & Parsing / Models
# Used By: Prescription Parser & Extractor
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel, Field


class RawPrescriptionItem(BaseModel):
    """Raw extracted medicine record from prescription OCR."""

    raw_text: str
    medicine_name_raw: str
    dosage: str = Field(default="As prescribed")
    frequency_raw: str = Field(default="OD")
    food_instruction_raw: str = Field(default="PC")
    duration_raw: str = Field(default="7 days")
    ocr_confidence: float = Field(default=1.0)


class PrescriptionParseResult(BaseModel):
    """Result of prescription parsing."""

    success: bool
    source_filename: str
    extraction_method: str
    items: List[RawPrescriptionItem] = Field(default_factory=list)
    raw_ocr_text: str = Field(default="")
    error_message: Optional[str] = None
