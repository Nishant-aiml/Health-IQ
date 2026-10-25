# --------------------------------------------------
# File: builder.py
# Purpose: Patient Timeline Builder constructing chronological milestone events.
# Module: Timeline Generator / Builder
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from backend.app.models.timeline_event import TimelineEvent
from backend.app.history.timeline.models import PatientTimeline, TimelineEventItem


class TimelineBuilder:
    """Assembles patient timeline events into PatientTimeline data object."""

    def build_timeline(self, user_id: int, events: List[TimelineEvent]) -> PatientTimeline:
        items = [
            TimelineEventItem(
                event_id=e.id,
                event_type=e.event_type if isinstance(e.event_type, str) else e.event_type.value,
                title=e.title,
                description=e.description,
                event_date=e.event_date,
                severity_level=e.severity_level,
                icon_hint=e.icon_hint,
            )
            for e in sorted(events, key=lambda ev: ev.event_date, reverse=True)
        ]

        return PatientTimeline(
            user_id=user_id,
            total_events=len(items),
            events=items,
        )


timeline_builder = TimelineBuilder()
