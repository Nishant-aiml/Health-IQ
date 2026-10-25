# --------------------------------------------------
# File: models.py
# Purpose: Domain models for structured nutrition recommendations (Increase, Reduce, Maintain, Monitor).
# Module: Nutrition Recommendation Engine / Models
# Used By: Generator & Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field


class NutritionActionType(str, Enum):
    INCREASE = "INCREASE"
    REDUCE = "REDUCE"
    MAINTAIN = "MAINTAIN"
    MONITOR = "MONITOR"


class NutritionRecommendationItem(BaseModel):
    action: NutritionActionType
    target_food_or_group: str
    category: str = Field(default="Dietary Guidance")
    reasoning: str
    biomarker_trigger: str
    supporting_evidence: str = "WHO / ICMR Clinical Nutrition Guidelines"
    limitations: str = "Educational dietary guidance; consult your dietitian or physician."
    priority: str = Field(default="MEDIUM", description="HIGH, MEDIUM, LOW")


class NutritionRecommendationBundle(BaseModel):
    report_id: int
    user_id: int
    recommendations: List[NutritionRecommendationItem] = Field(default_factory=list)
    overall_dietary_focus: str
