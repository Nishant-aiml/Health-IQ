# --------------------------------------------------
# File: registry.py
# Purpose: History Registry central interface.
# Module: History Intelligence
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.repository import history_repository, HistoryRepository
from backend.app.history.loader import historical_loader, HistoricalDataLoader


class HistoryRegistry:
    def get_repository(self) -> HistoryRepository:
        return history_repository


history_registry = HistoryRegistry()
