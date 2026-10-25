# --------------------------------------------------
# File: anemia.py
# Purpose: Microcytic and Macrocytic Anemia pattern detection rules.
# Module: Analysis Engine / Patterns
# Used By: Pattern Registry
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Dict, Optional, Any
from backend.app.analysis.patterns.base import PatternRule


class AnemiaPatternRule(PatternRule):
    def __init__(self):
        super().__init__(pattern_name="Anemia Pattern")

    def evaluate(self, extracted_parameters: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        hb = extracted_parameters.get("Hemoglobin")
        mcv = extracted_parameters.get("Mean Corpuscular Volume")

        if not hb:
            return None

        hb_val = hb["value"]
        hb_low = hb.get("normal_range_low") or 12.0

        if hb_val < hb_low:
            triggered_by = ["Hemoglobin"]
            pattern_subtype = "Anemia Pattern"
            summary_desc = "Low Hemoglobin levels detected."

            if mcv:
                mcv_val = mcv["value"]
                if mcv_val < 80.0:
                    pattern_subtype = "Microcytic Anemia Pattern"
                    triggered_by.append("Mean Corpuscular Volume")
                    summary_desc = "Combined low Hemoglobin and low MCV suggesting microcytic (iron-deficiency type) anemia pattern."
                elif mcv_val > 100.0:
                    pattern_subtype = "Macrocytic Anemia Pattern"
                    triggered_by.append("Mean Corpuscular Volume")
                    summary_desc = "Combined low Hemoglobin and elevated MCV suggesting macrocytic (B12/Folate deficiency type) anemia pattern."

            return {
                "pattern_name": pattern_subtype,
                "confidence": "high",
                "triggered_by": triggered_by,
                "summary": summary_desc,
            }

        return None
