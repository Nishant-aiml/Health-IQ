# --------------------------------------------------
# File: thrombocyte.py
# Purpose: Thrombocytopenia pattern detection rules.
# Module: Analysis Engine / Patterns
# Used By: Pattern Registry
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Dict, Optional, Any
from backend.app.analysis.patterns.base import PatternRule


class ThrombocytePatternRule(PatternRule):
    def __init__(self):
        super().__init__(pattern_name="Thrombocytopenia Pattern")

    def evaluate(self, extracted_parameters: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        plt = extracted_parameters.get("Platelet Count")
        if not plt:
            return None

        plt_val = plt["value"]
        plt_low = plt.get("normal_range_low") or 150.0

        if plt_val < plt_low:
            return {
                "pattern_name": "Thrombocytopenia Risk Pattern",
                "confidence": "high",
                "triggered_by": ["Platelet Count"],
                "summary": "Low platelet count detected below normal reference baseline.",
            }

        return None
