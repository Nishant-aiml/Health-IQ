# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Nutrition Recommendation Engine.
# Module: Nutrition Recommendation Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.nutrition.recommendations.generator import nutrition_recommendation_generator, NutritionRecommendationGenerator


class NutritionRecommendationRegistry:
    def generate_recommendations(self, report_id, user_id, extracted_values, historical_trends, prescription_drugs):
        return nutrition_recommendation_generator.generate_recommendations(
            report_id, user_id, extracted_values, historical_trends, prescription_drugs
        )


nutrition_recommendation_registry = NutritionRecommendationRegistry()
