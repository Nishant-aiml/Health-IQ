# --------------------------------------------------
# File: metabolic.py
# Purpose: Pre-Diabetes and Metabolic Syndrome pattern detection rules.
# Module: Analysis Engine / Patterns
# Used By: Pattern Registry
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Dict, Optional, Any
from backend.app.analysis.patterns.base import PatternRule


class MetabolicPatternRule(PatternRule):
    def __init__(self):
        super().__init__(pattern_name="Metabolic Risk Pattern")

    def evaluate(self, extracted_parameters: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        fbs = extracted_parameters.get("Fasting Blood Sugar")
        tg = extracted_parameters.get("Triglycerides")
        chol = extracted_parameters.get("Total Cholesterol")

        triggered_by = []
        is_fbs_high = False
        is_lipid_high = False

        if fbs and fbs["value"] > (fbs.get("normal_range_high") or 99.0):
            is_fbs_high = True
            triggered_by.append("Fasting Blood Sugar")

        if tg and tg["value"] > (tg.get("normal_range_high") or 149.0):
            is_lipid_high = True
            triggered_by.append("Triglycerides")

        if chol and chol["value"] > (chol.get("normal_range_high") or 199.0):
            is_lipid_high = True
            if "Total Cholesterol" not in triggered_by:
                triggered_by.append("Total Cholesterol")

        if is_fbs_high and is_lipid_high:
            return {
                "pattern_name": "Metabolic Syndrome Risk Pattern",
                "confidence": "high",
                "triggered_by": triggered_by,
                "summary": "Correlated elevation in fasting glucose and blood lipids indicating metabolic pattern risk.",
            }
        elif is_fbs_high:
            return {
                "pattern_name": "Impaired Fasting Glucose Pattern",
                "confidence": "moderate",
                "triggered_by": triggered_by,
                "summary": "Elevated fasting blood sugar levels above normal reference baselines.",
            }

        return None
