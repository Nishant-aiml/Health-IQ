# --------------------------------------------------
# File: trend.py
# Purpose: TrendSnapshot database table and TrendSeries domain models.
# Module: Core Database Models
# Used By: History Service & Trend Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional, List
from datetime import datetime, timezone
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class TrendSnapshot(SQLModel, table=True):
    __tablename__ = "trend_snapshots"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    parameter_canonical_name: str = Field(index=True)
    report_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    value: float
    unit: str = Field(default="mg/dL")
    direction: str = Field(default="stable", description="increasing, decreasing, stable, rapid_change, oscillation, recovery, persistent_abnormality")
    magnitude: float = Field(default=0.0)
    rate_of_change: float = Field(default=0.0)
    confidence: str = Field(default="HIGH", description="HIGH, MEDIUM, LOW")


class TrendSeries(BaseModel):
    """Domain model grouping a parameter's historical snapshots for series analysis."""

    canonical_name: str
    unit: str
    snapshots: List[TrendSnapshot] = []
