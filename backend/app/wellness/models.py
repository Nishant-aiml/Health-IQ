# --------------------------------------------------
# File: models.py
# Purpose: Domain models for Wellness Score Breakdown (Nutrition, Lifestyle, Hydration, Sleep, Overall Wellness Score).
# Module: Wellness Score Engine / Models
# Used By: Calculator & Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from pydantic import BaseModel, Field


class WellnessScoreBreakdown(BaseModel):
    report_id: int
    user_id: int
    health_score_reused: float = Field(..., description="Reused Phase 2B Health Score baseline")
    nutrition_score: float = Field(..., description="0-100 Nutrition Quality Score")
    lifestyle_score: float = Field(..., description="0-100 Activity & Movement Score")
    hydration_score: float = Field(..., description="0-100 Fluid Balance Score")
    sleep_score: float = Field(..., description="0-100 Sleep & Circadian Score")
    overall_wellness_score: float = Field(..., description="0-100 Transparent Overall Wellness Score")
    formula_explanation: str = Field(default="Weighted composite: Health Score (40%), Nutrition (25%), Lifestyle (15%), Hydration (10%), Sleep (10%).")
