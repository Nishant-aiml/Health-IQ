# --------------------------------------------------
# File: models.py
# Purpose: Domain models for trend-aware longitudinal recommendations.
# Module: Trend-aware Recommendations / Models
# Used By: Recommendation Generator
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from pydantic import BaseModel, Field


class TrendRecommendationItem(BaseModel):
    """Trend-aware extended recommendation record."""

    canonical_name: str
    category: str = Field(default="Lifestyle & Monitoring")
    priority: str = Field(default="MEDIUM", description="HIGH, MEDIUM, LOW")
    trend_context: str
    actionable_guidance: str
    doctor_question: str
    evidence_source: str = Field(default="Longitudinal Clinical Guidelines")
