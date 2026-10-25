# --------------------------------------------------
# File: test_timeline.py
# Purpose: Unit tests for timeline event builder and typed events.
# Module: Backend Test Suite / Timeline Generator
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from datetime import datetime
from backend.app.models.timeline_event import TimelineEvent, TimelineEventType
from backend.app.history.timeline.builder import timeline_builder


def test_timeline_builder_events():
    now = datetime.now()
    events = [
        TimelineEvent(id=1, user_id=1, event_type=TimelineEventType.UPLOAD, title="Upload 1", description="Desc 1", event_date=now),
        TimelineEvent(id=2, user_id=1, event_type=TimelineEventType.ALERT_CREATED, title="Alert 1", description="Desc 2", event_date=now),
    ]

    timeline = timeline_builder.build_timeline(1, events)
    assert timeline.total_events == 2
    assert timeline.events[0].event_type == "UPLOAD"
