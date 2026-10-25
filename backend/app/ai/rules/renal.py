# --------------------------------------------------
# File: renal.py
# Purpose: Clinical recommendation rule engine for Renal & Kidney parameters.
# Module: AI Engine / Rules
# Used By: Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel


class RenalRecommendationRule(ClinicalRule):
    def __init__(self):
        super().__init__(rule_name="Renal Clinical Rule")

    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs: List[Recommendation] = []
        creat = extracted_parameters.get("Serum Creatinine")

        if creat and creat.get("value", 0) > (creat.get("normal_range_high") or 1.35):
            val = creat["value"]
            severity = creat.get("severity", "mild")
            prio = PriorityLevel.CRITICAL if val > 3.0 else PriorityLevel.HIGH

            recs.append(
                Recommendation(
                    recommendation_id="RENAL_CREATININE_HIGH",
                    title="Renal Function Assessment & Hydration Protocol",
                    summary="Ensure optimal hydration, avoid nephrotoxic NSAIDs (ibuprofen), and consult a nephrologist.",
                    explanation="Serum creatinine is a byproduct of muscle metabolism filtered by the kidneys. Elevated levels suggest reduced glomerular filtration capacity.",
                    severity=severity,
                    priority=prio,
                    category="medical_followup",
                    supporting_parameters=["Serum Creatinine"],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="RenalRecommendationRule",
                )
            )

        return recs
