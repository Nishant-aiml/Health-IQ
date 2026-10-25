# --------------------------------------------------
# File: __init__.py
# Purpose: Food-Medicine Interaction Engine package index.
# Module: Food-Medicine Interaction Engine
# Used By: Services & Application
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.interactions.models import FoodMedicineInteraction, InteractionSeverity
from backend.app.nutrition.interactions.checker import FoodMedicineInteractionChecker, food_medicine_interaction_checker
from backend.app.nutrition.interactions.registry import FoodMedicineInteractionRegistry, food_medicine_interaction_registry

__all__ = [
    "FoodMedicineInteraction",
    "InteractionSeverity",
    "FoodMedicineInteractionChecker",
    "food_medicine_interaction_checker",
    "FoodMedicineInteractionRegistry",
    "food_medicine_interaction_registry",
]
