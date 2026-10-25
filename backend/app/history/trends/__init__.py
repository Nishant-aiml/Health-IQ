# --------------------------------------------------
# File: __init__.py
# Purpose: Trend Detection Engine package index.
# Module: Trend Detection Engine
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.trends.models import TrendEvidence, TrendAnalysisResult
from backend.app.history.trends.rules import evaluate_trend_direction
from backend.app.history.trends.analyzer import TrendAnalyzer, trend_analyzer
from backend.app.history.trends.registry import TrendRegistry, trend_registry

__all__ = [
    "TrendEvidence",
    "TrendAnalysisResult",
    "evaluate_trend_direction",
    "TrendAnalyzer",
    "trend_analyzer",
    "TrendRegistry",
    "trend_registry",
]
