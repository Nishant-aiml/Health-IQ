# --------------------------------------------------
# File: __init__.py
# Purpose: Nutrition Recommendation Engine package index.
# Module: Nutrition Recommendation Engine
# Used By: Services & Application
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.recommendations.models import NutritionRecommendationItem, NutritionActionType, NutritionRecommendationBundle
from backend.app.nutrition.recommendations.generator import NutritionRecommendationGenerator, nutrition_recommendation_generator
from backend.app.nutrition.recommendations.registry import NutritionRecommendationRegistry, nutrition_recommendation_registry

__all__ = [
    "NutritionRecommendationItem",
    "NutritionActionType",
    "NutritionRecommendationBundle",
    "NutritionRecommendationGenerator",
    "nutrition_recommendation_generator",
    "NutritionRecommendationRegistry",
    "nutrition_recommendation_registry",
]
