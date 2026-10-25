# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Food-Medicine Interaction Engine.
# Module: Food-Medicine Interaction Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.interactions.checker import food_medicine_interaction_checker, FoodMedicineInteractionChecker


class FoodMedicineInteractionRegistry:
    def check_interactions(self, active_prescription_drugs):
        return food_medicine_interaction_checker.check_interactions(active_prescription_drugs)


food_medicine_interaction_registry = FoodMedicineInteractionRegistry()
