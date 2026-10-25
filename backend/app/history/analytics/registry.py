# --------------------------------------------------
# File: registry.py
# Purpose: Time-Series Analytics Engine registry.
# Module: Time-Series Analytics
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.analytics.statistics import time_series_statistics_engine, TimeSeriesStatisticsEngine


class AnalyticsRegistry:
    def compute_statistics(self, canonical_name, readings):
        return time_series_statistics_engine.compute_statistics(canonical_name, readings)


analytics_registry = AnalyticsRegistry()
