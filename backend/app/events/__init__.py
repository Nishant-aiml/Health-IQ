# --------------------------------------------------
# File: __init__.py
# Purpose: Events package index.
# Module: Event Infrastructure
# Used By: Application Core
# Future Phase: Phase 2A
# --------------------------------------------------

from backend.app.events.base import EventBus, event_bus

__all__ = ["EventBus", "event_bus"]
