# --------------------------------------------------
# File: models.py
# Purpose: Domain models for Food-Medicine Interactions, severities, and timing advice.
# Module: Food-Medicine Interaction Engine / Models
# Used By: Checker & Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field


class InteractionSeverity(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class FoodMedicineInteraction(BaseModel):
    drug_name: str
    interacting_food_or_substance: str
    severity: InteractionSeverity
    mechanism_and_reason: str
    actionable_timing_guidance: str
    evidence_level: str = "Clinical Pharmacology Reference"
