# --------------------------------------------------
# File: models.py
# Purpose: Domain models for descriptive time-series statistics and variability metrics.
# Module: Time-Series Analytics / Models
# Used By: Analytics Engine & Trend Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from pydantic import BaseModel, Field


class AnalyticsResult(BaseModel):
    """Descriptive statistical summary for a historical biomarker time-series."""

    canonical_name: str
    unit: str
    sample_count: int
    mean_value: float
    median_value: float
    min_value: float
    max_value: float
    std_dev: float
    rate_of_change_per_month: float = Field(default=0.0)
    variability_index: float = Field(default=0.0, description="Coeff of Variation (%): (std_dev / mean) * 100")
    variability_level: str = Field(default="LOW", description="LOW, MODERATE, HIGH")
