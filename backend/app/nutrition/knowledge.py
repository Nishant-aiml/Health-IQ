# --------------------------------------------------
# File: knowledge.py
# Purpose: Nutrition Knowledge Engine repository manager uniting foods, nutrients, meal patterns, and hydration.
# Module: Nutrition Knowledge Engine / Knowledge Base
# Used By: Service Layer & Recommendation Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Optional, Any
from backend.app.nutrition.models import FoodItem, MicronutrientInfo
from backend.app.nutrition.foods import FOOD_DATABASE
from backend.app.nutrition.nutrients import MICRONUTRIENT_DATABASE, get_recommended_macronutrient_ratio
from backend.app.nutrition.meal_patterns import generate_circadian_meal_patterns, CircadianMealGuidance
from backend.app.nutrition.hydration import calculate_personalized_hydration, HydrationGuidanceTarget


class NutritionKnowledgeBase:
    """Central repository for clinical nutrition knowledge, food profiles, and hydration guidelines."""

    def get_food(self, food_id: str) -> Optional[FoodItem]:
        return FOOD_DATABASE.get(food_id.lower())

    def get_all_foods(self) -> List[FoodItem]:
        return list(FOOD_DATABASE.values())

    def get_nutrient_info(self, nutrient_name: str) -> Optional[MicronutrientInfo]:
        return MICRONUTRIENT_DATABASE.get(nutrient_name)

    def get_macronutrient_guidance(self, lab_summary: Dict[str, Any]):
        return get_recommended_macronutrient_ratio(lab_summary)

    def get_meal_patterns(self, lab_summary: Dict[str, Any]) -> CircadianMealGuidance:
        return generate_circadian_meal_patterns(lab_summary)

    def get_hydration_guidance(self, user_profile: Dict[str, Any], lab_summary: Dict[str, Any]) -> HydrationGuidanceTarget:
        return calculate_personalized_hydration(user_profile, lab_summary)


nutrition_knowledge_base = NutritionKnowledgeBase()
