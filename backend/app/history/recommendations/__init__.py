# --------------------------------------------------
# File: __init__.py
# Purpose: Trend-aware Recommendations package index.
# Module: Trend-aware Recommendations
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.recommendations.models import TrendRecommendationItem
from backend.app.history.recommendations.generator import TrendRecommendationGenerator, trend_recommendation_generator
from backend.app.history.recommendations.registry import TrendRecommendationRegistry, trend_recommendation_registry

__all__ = [
    "TrendRecommendationItem",
    "TrendRecommendationGenerator",
    "trend_recommendation_generator",
    "TrendRecommendationRegistry",
    "trend_recommendation_registry",
]
