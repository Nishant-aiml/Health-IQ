# --------------------------------------------------
# File: models.py
# Purpose: Domain models for pharmacology knowledge items and confidence scores.
# Module: Medicine Intelligence / Models
# Used By: Medicine Knowledge Base & Resolution Pipeline
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel, Field


class MedicineInfo(BaseModel):
    """
    Complete pharmacology knowledge representation for a medicine.
    """

    generic_name: str
    brand_name: Optional[str] = None
    brand_names: List[str] = Field(default_factory=list)
    active_ingredient: str
    drug_class: str
    category: str
    purpose: str
    mechanism: str
    common_uses: List[str] = Field(default_factory=list)
    adult_dosage: str = Field(default="As prescribed by physician")
    pediatric_notes: Optional[str] = Field(default="Consult pediatrician for dose adjustment.")
    pregnancy_warning: str = Field(default="Consult doctor before use during pregnancy.")
    pregnancy_category: str = Field(default="B", description="A, B, C, D, X")
    storage: str = Field(default="Store below 30°C in a cool, dry place away from direct sunlight.")
    side_effects: List[str] = Field(default_factory=list)
    contraindications: List[str] = Field(default_factory=list)
    common_interactions: List[str] = Field(default_factory=list)
    food_warnings: List[str] = Field(default_factory=list)
    alcohol_warning: str = Field(default="Avoid alcohol consumption while taking this medication.")
    driving_warning: str = Field(default="May cause mild drowsiness. Caution while driving.")
    ocr_confidence: float = Field(default=1.0)
    resolution_confidence: float = Field(default=1.0)
    knowledge_confidence: float = Field(default=1.0)
    is_unknown: bool = Field(default=False)
    possible_matches: List[str] = Field(default_factory=list)
