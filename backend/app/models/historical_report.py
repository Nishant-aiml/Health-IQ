# --------------------------------------------------
# File: historical_report.py
# Purpose: SQLModel table storing historical report metadata and health score evolution.
# Module: Core Database Models
# Used By: History Service & Timeline Generator
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class HistoricalReport(SQLModel, table=True):
    __tablename__ = "historical_reports"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    source_filename: str = Field(default="report.pdf")
    doc_type: str = Field(default="lab_report", description="lab_report, prescription, discharge_summary")
    collection_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    health_score: float = Field(default=100.0)
    total_parameters: int = Field(default=0)
    abnormal_parameters_count: int = Field(default=0)
    critical_alerts_count: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
