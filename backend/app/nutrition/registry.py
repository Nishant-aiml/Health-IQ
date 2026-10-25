# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Nutrition Knowledge Engine.
# Module: Nutrition Knowledge Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.knowledge import nutrition_knowledge_base, NutritionKnowledgeBase


class NutritionRegistry:
    def get_knowledge_base(self) -> NutritionKnowledgeBase:
        return nutrition_knowledge_base


nutrition_registry = NutritionRegistry()
