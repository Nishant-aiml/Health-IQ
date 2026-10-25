# --------------------------------------------------
# File: checker.py
# Purpose: Food-Medicine Interaction Checker evaluating active prescriptions against clinical rules.
# Module: Food-Medicine Interaction Engine / Checker
# Used By: Nutrition Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List
from backend.app.nutrition.interactions.models import FoodMedicineInteraction
from backend.app.nutrition.interactions.rules import CLINICAL_FOOD_DRUG_RULES


class FoodMedicineInteractionChecker:
    """Evaluates active prescriptions against food-drug interaction rules."""

    def check_interactions(self, active_prescription_drugs: List[str]) -> List[FoodMedicineInteraction]:
        flagged: List[FoodMedicineInteraction] = []

        normalized_drugs = [d.lower() for d in active_prescription_drugs]

        for rule in CLINICAL_FOOD_DRUG_RULES:
            rule_drug = rule.drug_name.lower()
            if any(rule_drug in nd for nd in normalized_drugs):
                flagged.append(rule)

        return flagged


food_medicine_interaction_checker = FoodMedicineInteractionChecker()
