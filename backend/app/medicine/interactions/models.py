# --------------------------------------------------
# File: models.py
# Purpose: Domain models for drug interactions, duplicate therapy, and safety warnings.
# Module: Medicine Interaction Engine / Models
# Used By: Interaction Rules & Safety Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel, Field


class DrugInteractionItem(BaseModel):
    """Represents a specific drug interaction or safety risk."""

    drug_a: str
    drug_b: Optional[str] = None
    severity: str = Field(default="MEDIUM", description="HIGH, MEDIUM, LOW")
    interaction_type: str = Field(default="drug_drug", description="drug_drug, duplicate, food, pregnancy, alcohol, driving")
    title: str
    description: str
    recommendation: str
    evidence_source: str = Field(default="WHO Pharmacology / Clinical Guidelines")


class SafetyResult(BaseModel):
    """Aggregated clinical safety analysis for a list of prescribed medicines."""

    interactions: List[DrugInteractionItem] = Field(default_factory=list)
    duplicate_therapies: List[DrugInteractionItem] = Field(default_factory=list)
    food_warnings: List[DrugInteractionItem] = Field(default_factory=list)
    pregnancy_warnings: List[DrugInteractionItem] = Field(default_factory=list)
    alcohol_warnings: List[DrugInteractionItem] = Field(default_factory=list)
    driving_warnings: List[DrugInteractionItem] = Field(default_factory=list)
    monitoring_notes: List[str] = Field(default_factory=list)
    has_high_risk: bool = Field(default=False)
