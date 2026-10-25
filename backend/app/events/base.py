# --------------------------------------------------
# File: base.py
# Purpose: Event Bus & Domain Event Dispatcher placeholder.
# Module: Event Infrastructure
# Used By: Queue Workers, Notification Engines
# Future Phase: Phase 2A Ingestion & Future Event Hooks
# --------------------------------------------------

from typing import Dict, List, Callable, Any, Awaitable
from backend.app.core.logging import logger

EventHandler = Callable[[Dict[str, Any]], Awaitable[None]]


class EventBus:
    """
    Decoupled Event Bus for dispatching domain events.

    Why it exists:
        Allows background tasks (like OCR completion or job finalization) to emit
        events without directly coupling worker logic to downstream listeners.
    """

    def __init__(self):
        self._subscribers: Dict[str, List[EventHandler]] = {}

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        """Subscribes an async handler to a specific event type."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    async def publish(self, event_type: str, payload: Dict[str, Any]) -> None:
        """Publishes an event to all subscribed handlers."""
        handlers = self._subscribers.get(event_type, [])
        logger.info(f"Publishing event '{event_type}' to {len(handlers)} handlers.")
        for handler in handlers:
            try:
                await handler(payload)
            except Exception as e:
                logger.error(f"Error executing handler for event '{event_type}': {e}")


event_bus = EventBus()
