# --------------------------------------------------
# File: generator.py
# Purpose: ELI10 (Explain Like I'm 10) plain-language child-friendly explanation generator.
# Module: AI Engine / ELI10
# Used By: Recommendation Service
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import Dict, Any
from backend.app.ai.eli10.templates import ELI10_TEMPLATES


class ELI10Generator:
    """
    ELI10 Generator.

    Why it exists:
        Translates complex clinical terminology ("Hemoglobin below normal reference interval")
        into simple, non-alarmist, child-friendly explanations ("Tiny oxygen delivery trucks").
    """

    def generate_explanation(self, extracted_parameters: Dict[str, Any]) -> str:
        explanation_parts = []

        for p_name, param_info in extracted_parameters.items():
            if param_info.get("severity", "normal") != "normal":
                if p_name in ELI10_TEMPLATES:
                    explanation_parts.append(ELI10_TEMPLATES[p_name])

        if not explanation_parts:
            return "Your blood test results look happy and healthy! All your body's energy trucks and filters are working normally."

        return " ".join(explanation_parts)


eli10_generator = ELI10Generator()
