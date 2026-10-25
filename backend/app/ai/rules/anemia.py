# --------------------------------------------------
# File: anemia.py
# Purpose: Clinical recommendation rule engine for Anemia and Low Hemoglobin.
# Module: AI Engine / Rules
# Used By: Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel


class AnemiaRecommendationRule(ClinicalRule):
    def __init__(self):
        super().__init__(rule_name="Anemia Clinical Rule")

    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs: List[Recommendation] = []
        hb = extracted_parameters.get("Hemoglobin")

        if not hb:
            return recs

        hb_val = hb.get("value", 15.0)
        hb_low = hb.get("normal_range_low") or 13.8
        severity = hb.get("severity", "normal")

        if hb_val < hb_low:
            is_microcytic = any(p.get("pattern_name") == "Microcytic Anemia Pattern" for p in detected_patterns)
            
            prio = PriorityLevel.HIGH
            if severity == "severe" or hb.get("is_critical"):
                prio = PriorityLevel.CRITICAL

            explanation_text = "Hemoglobin is the primary protein in red blood cells that carries oxygen throughout your body."
            if is_microcytic:
                explanation_text += " Low Hemoglobin combined with low MCV points toward iron-deficiency microcytic anemia."

            recs.append(
                Recommendation(
                    recommendation_id="ANEMIA_LOW_HB",
                    title="Dietary & Diagnostic Iron Evaluation",
                    summary="Incorporate iron-rich dietary sources and consult a physician for a serum ferritin panel.",
                    explanation=explanation_text,
                    severity=severity,
                    priority=prio,
                    category="medical_followup",
                    supporting_parameters=["Hemoglobin"],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="AnemiaRecommendationRule",
                )
            )

        return recs
