# --------------------------------------------------
# File: __init__.py
# Purpose: Time-Series Analytics Engine package index.
# Module: Time-Series Analytics
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.analytics.models import AnalyticsResult
from backend.app.history.analytics.variability import calculate_variability
from backend.app.history.analytics.statistics import TimeSeriesStatisticsEngine, time_series_statistics_engine
from backend.app.history.analytics.registry import AnalyticsRegistry, analytics_registry

__all__ = [
    "AnalyticsResult",
    "calculate_variability",
    "TimeSeriesStatisticsEngine",
    "time_series_statistics_engine",
    "AnalyticsRegistry",
    "analytics_registry",
]
