# --------------------------------------------------
# File: medicine_interaction.py
# Purpose: Normalized SQLModel table storing drug-drug and drug-safety interactions.
# Module: Core Database Models
# Used By: Medicine Interaction Engine & API Controllers
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Optional
from sqlmodel import SQLModel, Field


class MedicineInteraction(SQLModel, table=True):
    __tablename__ = "medicine_interactions"

    id: Optional[int] = Field(default=None, primary_key=True)
    prescription_id: int = Field(foreign_key="prescriptions.id", index=True)
    drug_a: str
    drug_b: Optional[str] = None
    severity: str = Field(default="MEDIUM", description="HIGH, MEDIUM, LOW")
    interaction_type: str = Field(default="drug_drug", description="drug_drug, duplicate, food, pregnancy, alcohol, driving")
    title: str
    description: str
    recommendation: str
    evidence_source: Optional[str] = Field(default="WHO Pharmacology / Clinical Guidelines")
