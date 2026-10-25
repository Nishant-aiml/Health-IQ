# --------------------------------------------------
# File: metabolic.py
# Purpose: Clinical recommendation rule engine for Metabolic & Blood Glucose parameters.
# Module: AI Engine / Rules
# Used By: Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.rules.base import ClinicalRule
from backend.app.ai.models import Recommendation, PriorityLevel, ConfidenceLevel


class MetabolicRecommendationRule(ClinicalRule):
    def __init__(self):
        super().__init__(rule_name="Metabolic Clinical Rule")

    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        recs: List[Recommendation] = []
        fbs = extracted_parameters.get("Fasting Blood Sugar")
        chol = extracted_parameters.get("Total Cholesterol")

        if fbs and fbs.get("value", 0) > (fbs.get("normal_range_high") or 99.0):
            val = fbs["value"]
            severity = fbs.get("severity", "mild")
            prio = PriorityLevel.HIGH if val > 126.0 else PriorityLevel.MEDIUM

            recs.append(
                Recommendation(
                    recommendation_id="METABOLIC_GLUCOSE_ELEVATED",
                    title="Glycemic Management & Dietary Fiber Enhancement",
                    summary="Monitor carbohydrate intake, adopt a low-glycemic index diet, and recheck HbA1c.",
                    explanation="Elevated fasting blood sugar indicates glucose regulation stress. Incorporating soluble fiber and post-meal walks helps optimize insulin sensitivity.",
                    severity=severity,
                    priority=prio,
                    category="dietary",
                    supporting_parameters=["Fasting Blood Sugar"],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="MetabolicRecommendationRule",
                )
            )

        if chol and chol.get("value", 0) > (chol.get("normal_range_high") or 199.0):
            recs.append(
                Recommendation(
                    recommendation_id="LIPID_CHOLESTEROL_HIGH",
                    title="Cardiovascular Lipid Profile Optimization",
                    summary="Reduce saturated fats, increase Omega-3 fatty acids, and maintain active aerobic exercise.",
                    explanation="Total cholesterol above 200 mg/dL increases lipid plaque risk. Lifestyle adjustments improve HDL/LDL ratios.",
                    severity=chol.get("severity", "mild"),
                    priority=PriorityLevel.MEDIUM,
                    category="lifestyle",
                    supporting_parameters=["Total Cholesterol"],
                    confidence=ConfidenceLevel.HIGH,
                    recommendation_type="rule_based",
                    generated_by="MetabolicRecommendationRule",
                )
            )

        return recs
