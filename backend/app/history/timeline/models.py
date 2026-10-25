# --------------------------------------------------
# File: models.py
# Purpose: Domain models for patient timeline milestones and health journey snapshots.
# Module: Timeline Generator / Models
# Used By: Timeline Builder & History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimelineEventItem(BaseModel):
    """Single chronological event in patient health journey."""

    event_id: Optional[int] = None
    event_type: str
    title: str
    description: str
    event_date: datetime
    severity_level: str = Field(default="INFO")
    icon_hint: str = Field(default="activity")


class PatientTimeline(BaseModel):
    """Complete chronological patient health journey timeline."""

    user_id: int
    total_events: int
    events: List[TimelineEventItem] = Field(default_factory=list)
