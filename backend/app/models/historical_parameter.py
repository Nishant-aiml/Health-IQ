# --------------------------------------------------
# File: historical_parameter.py
# Purpose: SQLModel table storing canonicalized historical biomarker readings with reference range versioning.
# Module: Core Database Models
# Used By: History Service & Biomarker Alignment Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class HistoricalParameter(SQLModel, table=True):
    __tablename__ = "historical_parameters"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    canonical_name: str = Field(index=True)
    raw_name: str
    value: float
    unit: str
    lab_name: Optional[str] = Field(default="Standard Clinical Lab")
    reference_range_low: Optional[float] = None
    reference_range_high: Optional[float] = None
    range_version: str = Field(default="v1.0")
    severity: str = Field(default="NORMAL", description="NORMAL, ELEVATED, LOW, CRITICAL")
    collection_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
