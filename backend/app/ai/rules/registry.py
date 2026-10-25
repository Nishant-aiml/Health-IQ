# --------------------------------------------------
# File: registry.py
# Purpose: Recommendation Registry orchestrator executing rules and sorting output by priority.
# Module: AI Engine / Rules
# Used By: Recommendation Engine
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.rules.anemia import AnemiaRecommendationRule
from backend.app.ai.rules.metabolic import MetabolicRecommendationRule
from backend.app.ai.rules.renal import RenalRecommendationRule
from backend.app.ai.rules.thyroid import ThyroidRecommendationRule
from backend.app.ai.rules.liver import LiverRecommendationRule
from backend.app.ai.models import Recommendation, PriorityLevel
from backend.app.core.logging import logger


class RecommendationRegistry:
    """
    Recommendation Registry Orchestrator.

    Why it exists:
        Maintains an active registry of `ClinicalRule` instances. Executes all rules,
        deduplicates recommendations by `recommendation_id`, and sorts output by priority
        (`CRITICAL` > `HIGH` > `MEDIUM` > `LOW` > `INFORMATIONAL`).
    """

    def __init__(self, rules: List[ClinicalRule] = None):
        self.rules = rules or [
            AnemiaRecommendationRule(),
            MetabolicRecommendationRule(),
            RenalRecommendationRule(),
            ThyroidRecommendationRule(),
            LiverRecommendationRule(),
        ]

    def evaluate_all(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        raw_recs: List[Recommendation] = []

        for rule in self.rules:
            try:
                rule_results = rule.evaluate(extracted_parameters, detected_patterns)
                raw_recs.extend(rule_results)
            except Exception as exc:
                logger.error(f"Error executing recommendation rule '{rule.rule_name}': {exc}")

        # Deduplicate by recommendation_id
        seen_ids = set()
        unique_recs: List[Recommendation] = []
        for rec in raw_recs:
            if rec.recommendation_id not in seen_ids:
                seen_ids.add(rec.recommendation_id)
                unique_recs.append(rec)

        # Priority weight map for sorting
        prio_weights = {
            PriorityLevel.CRITICAL: 1,
            PriorityLevel.HIGH: 2,
            PriorityLevel.MEDIUM: 3,
            PriorityLevel.LOW: 4,
            PriorityLevel.INFORMATIONAL: 5,
        }

        # Sort recommendations by priority weight
        unique_recs.sort(key=lambda r: prio_weights.get(r.priority, 99))
        return unique_recs


recommendation_registry = RecommendationRegistry()
