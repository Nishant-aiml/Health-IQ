# --------------------------------------------------
# File: generator.py
# Purpose: Mandatory clinical context and limitation notice generator.
# Module: AI Engine / Limitations
# Used By: Recommendation Service
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List
from backend.app.ai.models import Limitation


class LimitationsGenerator:
    """
    Limitations Generator.

    Why it exists:
        Guarantees that every generated recommendation bundle includes mandatory clinical disclaimers.
        Prevents AI recommendations from being presented as medical diagnoses.
    """

    def generate_limitations(self, has_critical_alerts: bool = False) -> List[Limitation]:
        limitations = [
            Limitation(
                notice="This recommendation analysis is strictly informational and non-diagnostic.",
                disclaimer_type="legal_medical",
                clinical_context_required=True,
            ),
            Limitation(
                notice="Laboratory parameter values must be interpreted in conjunction with a patient's physical examination and medical history.",
                disclaimer_type="clinical_context",
                clinical_context_required=True,
            ),
            Limitation(
                notice="Consult a qualified healthcare professional before making any dietary, lifestyle, or medication changes.",
                disclaimer_type="action_disclaimer",
                clinical_context_required=True,
            ),
        ]

        if has_critical_alerts:
            limitations.append(
                Limitation(
                    notice="Critical medical values detected require immediate professional medical consultation.",
                    disclaimer_type="critical_emergency",
                    clinical_context_required=True,
                )
            )

        return limitations


limitations_generator = LimitationsGenerator()
