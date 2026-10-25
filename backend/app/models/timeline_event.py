# --------------------------------------------------
# File: timeline_event.py
# Purpose: SQLModel table storing typed chronological health journey milestones.
# Module: Core Database Models
# Used By: Timeline Builder & History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from datetime import datetime, timezone
from enum import Enum
from sqlmodel import SQLModel, Field


class TimelineEventType(str, Enum):
    UPLOAD = "UPLOAD"
    PATTERN_DETECTED = "PATTERN_DETECTED"
    PATTERN_RESOLVED = "PATTERN_RESOLVED"
    ALERT_CREATED = "ALERT_CREATED"
    ALERT_RESOLVED = "ALERT_RESOLVED"
    PRESCRIPTION_UPDATED = "PRESCRIPTION_UPDATED"
    HEALTH_SCORE_CHANGED = "HEALTH_SCORE_CHANGED"


class TimelineEvent(SQLModel, table=True):
    __tablename__ = "timeline_events"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    report_id: Optional[int] = Field(default=None, foreign_key="reports.id", index=True)
    event_type: TimelineEventType = Field(default=TimelineEventType.UPLOAD, index=True)
    title: str
    description: str
    event_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), index=True)
    severity_level: str = Field(default="INFO", description="INFO, WARNING, CRITICAL, SUCCESS")
    icon_hint: str = Field(default="activity")
