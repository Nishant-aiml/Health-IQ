# --------------------------------------------------
# File: registry.py
# Purpose: Trend Detection Engine registry.
# Module: Trend Detection Engine
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.trends.analyzer import trend_analyzer, TrendAnalyzer


class TrendRegistry:
    def analyze_series(self, canonical_name, readings):
        return trend_analyzer.analyze_series(canonical_name, readings)


trend_registry = TrendRegistry()
