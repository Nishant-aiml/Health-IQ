# --------------------------------------------------
# File: renal.py
# Purpose: Renal Stress pattern detection rules.
# Module: Analysis Engine / Patterns
# Used By: Pattern Registry
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Dict, Optional, Any
from backend.app.analysis.patterns.base import PatternRule


class RenalPatternRule(PatternRule):
    def __init__(self):
        super().__init__(pattern_name="Renal Stress Pattern")

    def evaluate(self, extracted_parameters: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        creat = extracted_parameters.get("Serum Creatinine")
        urea = extracted_parameters.get("Blood Urea") or extracted_parameters.get("Blood Urea Nitrogen")

        triggered_by = []
        is_creat_high = False
        is_urea_high = False

        if creat and creat["value"] > (creat.get("normal_range_high") or 1.35):
            is_creat_high = True
            triggered_by.append("Serum Creatinine")

        if urea and urea["value"] > (urea.get("normal_range_high") or 20.0):
            is_urea_high = True
            triggered_by.append(urea["canonical_name"] if "canonical_name" in urea else "Blood Urea")

        if is_creat_high and is_urea_high:
            return {
                "pattern_name": "Renal Stress Pattern",
                "confidence": "high",
                "triggered_by": triggered_by,
                "summary": "Combined elevation in serum creatinine and blood urea indicating kidney stress pattern.",
            }
        elif is_creat_high:
            return {
                "pattern_name": "Elevated Serum Creatinine Pattern",
                "confidence": "moderate",
                "triggered_by": triggered_by,
                "summary": "Serum creatinine elevated above normal reference baseline.",
            }

        return None
