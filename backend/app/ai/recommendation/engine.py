# --------------------------------------------------
# File: engine.py
# Purpose: Orchestrates recommendation generation across active clinical rule engines.
# Module: AI Engine / Recommendation
# Used By: Recommendation Service
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel
from backend.app.ai.rules import recommendation_registry
from backend.app.ai.recommendation.templates import DEFAULT_OPTIMAL_RECOMMENDATION


class RecommendationEngine:
    """
    Recommendation Engine Orchestrator.

    Why it exists:
        Transforms Phase 2B deterministic analysis outputs (parameters, severity, patterns)
        into structured, prioritized, explainable recommendations.
    """

    def generate_recommendations(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs = recommendation_registry.evaluate_all(extracted_parameters, detected_patterns)

        if not recs:
            recs.append(
                Recommendation(
                    recommendation_id=DEFAULT_OPTIMAL_RECOMMENDATION["recommendation_id"],
                    title=DEFAULT_OPTIMAL_RECOMMENDATION["title"],
                    summary=DEFAULT_OPTIMAL_RECOMMENDATION["summary"],
                    explanation=DEFAULT_OPTIMAL_RECOMMENDATION["explanation"],
                    severity=DEFAULT_OPTIMAL_RECOMMENDATION["severity"],
                    priority=PriorityLevel.INFORMATIONAL,
                    category=DEFAULT_OPTIMAL_RECOMMENDATION["category"],
                    confidence=ConfidenceLevel.VERY_HIGH,
                    recommendation_type=DEFAULT_OPTIMAL_RECOMMENDATION["recommendation_type"],
                    generated_by=DEFAULT_OPTIMAL_RECOMMENDATION["generated_by"],
                )
            )

        return recs


recommendation_engine = RecommendationEngine()
