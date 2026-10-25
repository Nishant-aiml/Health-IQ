# --------------------------------------------------
# File: __init__.py
# Purpose: Recommendation package index.
# Module: AI Engine / Recommendation
# Used By: Recommendation Service
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.recommendation.engine import RecommendationEngine, recommendation_engine

__all__ = [
    "RecommendationEngine",
    "recommendation_engine",
]
