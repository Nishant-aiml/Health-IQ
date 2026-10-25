# --------------------------------------------------
# File: models.py
# Purpose: Domain models for historical report snapshots, biomarker series, and clinical trends.
# Module: History Intelligence / Models
# Used By: History Repository & Trend Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class HistoricalParameterReading(BaseModel):
    """Single historical reading for a canonical lab parameter."""

    report_id: int
    collection_date: datetime
    raw_name: str
    canonical_name: str
    value: float
    unit: str
    lab_name: str = Field(default="Standard Clinical Lab")
    reference_range_low: Optional[float] = None
    reference_range_high: Optional[float] = None
    range_version: str = Field(default="v1.0")
    severity: str = Field(default="NORMAL")


class ParameterHistorySeries(BaseModel):
    """Historical timeline series for a single canonical biomarker across multiple reports."""

    canonical_name: str
    unit: str
    readings: List[HistoricalParameterReading] = Field(default_factory=list)
    available_reports: int = 0
