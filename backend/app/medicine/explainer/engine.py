# --------------------------------------------------
# File: engine.py
# Purpose: Medicine Explanation Engine orchestrating patient-friendly explanations, safety notes, and ELI10.
# Module: Medicine Explanation Engine / Core Engine
# Used By: Medicine Service
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Dict, Any
from backend.app.medicine.models import MedicineInfo
from backend.app.medicine.explainer.templates import EXPLANATION_TEMPLATE, EXPLANATION_DISCLAIMER
from backend.app.medicine.explainer.eli10 import generate_eli10_explanation


class MedicineExplainerEngine:
    """Generates structured, patient-friendly explanations and safety disclaimers."""

    def explain_medicine(self, medicine_info: MedicineInfo) -> Dict[str, Any]:
        food_w = medicine_info.food_warnings[0] if medicine_info.food_warnings else "Take as directed by doctor."
        uses_str = "\n- ".join(medicine_info.common_uses) if medicine_info.common_uses else medicine_info.purpose

        explanation_text = EXPLANATION_TEMPLATE.format(
            brand_name=medicine_info.brand_name or medicine_info.generic_name,
            generic_name=medicine_info.generic_name,
            active_ingredient=medicine_info.active_ingredient,
            drug_class=medicine_info.drug_class,
            purpose=medicine_info.purpose,
            mechanism=medicine_info.mechanism,
            common_uses=uses_str,
            adult_dosage=medicine_info.adult_dosage,
            food_warning=food_w,
            driving_warning=medicine_info.driving_warning,
            pregnancy_warning=medicine_info.pregnancy_warning,
            storage=medicine_info.storage,
        ).strip()

        eli10 = generate_eli10_explanation(
            medicine_info.generic_name,
            medicine_info.brand_name or medicine_info.generic_name,
        )

        return {
            "generic_name": medicine_info.generic_name,
            "brand_name": medicine_info.brand_name,
            "active_ingredient": medicine_info.active_ingredient,
            "explanation": explanation_text,
            "eli10": eli10,
            "disclaimer": EXPLANATION_DISCLAIMER,
        }


medicine_explainer_engine = MedicineExplainerEngine()
