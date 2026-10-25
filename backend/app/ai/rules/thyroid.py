# --------------------------------------------------
# File: thyroid.py
# Purpose: Clinical recommendation rule engine for Thyroid parameters.
# Module: AI Engine / Rules
# Used By: Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel


class ThyroidRecommendationRule(ClinicalRule):
    def __init__(self):
        super().__init__(rule_name="Thyroid Clinical Rule")

    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs: List[Recommendation] = []
        tsh = extracted_parameters.get("Thyroid Stimulating Hormone")

        if tsh and tsh.get("value", 0) > (tsh.get("normal_range_high") or 4.5):
            recs.append(
                Recommendation(
                    recommendation_id="THYROID_TSH_HIGH",
                    title="Thyroid Hormone Balance Evaluation",
                    summary="Consult an endocrinologist to evaluate free T3/T4 levels for hypothyroid screening.",
                    explanation="Elevated TSH indicates pituitary stimulation due to lower circulating thyroid hormone levels.",
                    severity=tsh.get("severity", "mild"),
                    priority=PriorityLevel.MEDIUM,
                    category="diagnostic",
                    supporting_parameters=["Thyroid Stimulating Hormone"],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="ThyroidRecommendationRule",
                )
            )

        return recs
