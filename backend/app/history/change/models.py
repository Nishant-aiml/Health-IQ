# --------------------------------------------------
# File: models.py
# Purpose: Domain models for report comparison modes (Previous, Baseline, Best, Custom Range) and biomarker change items.
# Module: Clinical Change Engine / Models
# Used By: Comparator & Change Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class ComparisonMode(str, Enum):
    PREVIOUS = "PREVIOUS"
    BASELINE = "BASELINE"
    BEST = "BEST"
    CUSTOM_RANGE = "CUSTOM_RANGE"


class BiomarkerChangeItem(BaseModel):
    """Detailed change comparison for a single canonical biomarker."""

    canonical_name: str
    unit: str
    target_value: float
    reference_value: float
    absolute_change: float
    percentage_change: float
    change_status: str = Field(..., description="Improved, Unchanged, Worsened")
    clinical_significance: str = Field(default="MODERATE", description="HIGH, MODERATE, LOW")
    summary_note: str


class ComparisonResult(BaseModel):
    """Comprehensive comparative analysis between target and reference reports."""

    comparison_mode: ComparisonMode
    target_report_id: int
    reference_report_id: int
    target_date: datetime
    reference_date: datetime
    health_score_delta: float
    improved_count: int
    unchanged_count: int
    worsened_count: int
    biomarker_changes: List[BiomarkerChangeItem] = Field(default_factory=list)
    overall_clinical_assessment: str
