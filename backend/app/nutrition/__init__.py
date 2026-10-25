# --------------------------------------------------
# File: __init__.py
# Purpose: Nutrition Knowledge Engine package index.
# Module: Nutrition Knowledge Engine
# Used By: Services & Application
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.models import FoodItem, FoodCategory, NutrientProfile, EvidenceLevel, MicronutrientInfo, MacronutrientRatio
from backend.app.nutrition.knowledge import NutritionKnowledgeBase, nutrition_knowledge_base
from backend.app.nutrition.registry import NutritionRegistry, nutrition_registry

__all__ = [
    "FoodItem",
    "FoodCategory",
    "NutrientProfile",
    "EvidenceLevel",
    "MicronutrientInfo",
    "MacronutrientRatio",
    "NutritionKnowledgeBase",
    "nutrition_knowledge_base",
    "NutritionRegistry",
    "nutrition_registry",
]
