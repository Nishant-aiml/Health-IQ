# --------------------------------------------------
# File: liver.py
# Purpose: Clinical recommendation rule engine for Liver Function parameters.
# Module: AI Engine / Rules
# Used By: Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel


class LiverRecommendationRule(ClinicalRule):
    def __init__(self):
        super().__init__(rule_name="Liver Clinical Rule")

    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs: List[Recommendation] = []
        alt = extracted_parameters.get("ALT") or extracted_parameters.get("SGPT")

        if alt and alt.get("value", 0) > (alt.get("normal_range_high") or 45.0):
            recs.append(
                Recommendation(
                    recommendation_id="LIVER_ALT_HIGH",
                    title="Hepatic Enzyme Activity Follow-up",
                    summary="Limit alcohol consumption, review medications with a doctor, and retest LFT panel.",
                    explanation="Elevated Alanine Aminotransferase (ALT) is a marker of hepatic cellular stress.",
                    severity=alt.get("severity", "mild"),
                    priority=PriorityLevel.MEDIUM,
                    category="medical_followup",
                    supporting_parameters=[alt.get("canonical_name", "ALT")],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="LiverRecommendationRule",
                )
            )

        return recs
