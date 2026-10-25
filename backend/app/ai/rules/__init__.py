# --------------------------------------------------
# File: __init__.py
# Purpose: AI Rules package index.
# Module: AI Engine / Rules
# Used By: Recommendation Engine
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.rules.registry import RecommendationRegistry, recommendation_registry

__all__ = [
    "ClinicalRule",
    "RecommendationRegistry",
    "recommendation_registry",
]
