# --------------------------------------------------
# File: registry.py
# Purpose: Trend-aware Recommendations Registry.
# Module: Trend-aware Recommendations
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.recommendations.generator import trend_recommendation_generator, TrendRecommendationGenerator


class TrendRecommendationRegistry:
    def generate_trend_recommendations(self, trend_results):
        return trend_recommendation_generator.generate_trend_recommendations(trend_results)


trend_recommendation_registry = TrendRecommendationRegistry()
