# --------------------------------------------------
# File: models.py
# Purpose: Domain models for deterministic trend results, confidence metrics, and rule evidence.
# Module: Trend Detection Engine / Models
# Used By: Trend Rules & Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TrendEvidence(BaseModel):
    """Transparent evidence metadata showing reports, values, and rule triggers."""

    report_dates: List[datetime] = Field(default_factory=list)
    values: List[float] = Field(default_factory=list)
    rule_triggered: str
    explanation: str


class TrendAnalysisResult(BaseModel):
    """Result of deterministic longitudinal trend detection."""

    canonical_name: str
    unit: str
    direction: str = Field(..., description="increasing, decreasing, stable, rapid_change, oscillation, recovery, persistent_abnormality")
    trend_confidence: str = Field(default="HIGH", description="HIGH, MEDIUM, LOW")
    available_reports: int = 0
    required_reports: int = 2
    percentage_change: float = 0.0
    absolute_change: float = 0.0
    evidence: TrendEvidence
    clinical_summary: str
