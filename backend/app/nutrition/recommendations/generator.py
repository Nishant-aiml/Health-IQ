# --------------------------------------------------
# File: generator.py
# Purpose: Nutrition Recommendation Generator compiling non-generic food guidance.
# Module: Nutrition Recommendation Engine / Generator
# Used By: Nutrition Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.nutrition.recommendations.models import NutritionRecommendationBundle
from backend.app.nutrition.recommendations.rules import evaluate_nutrition_rules


class NutritionRecommendationGenerator:
    """Generates personalized food recommendations based on lab values, trends, and medicines."""

    def generate_recommendations(
        self,
        report_id: int,
        user_id: int,
        extracted_values: List[Dict[str, Any]],
        historical_trends: List[Dict[str, Any]],
        prescription_drugs: List[str],
    ) -> NutritionRecommendationBundle:
        recs = evaluate_nutrition_rules(extracted_values, historical_trends, prescription_drugs)

        has_high_priority = any(r.priority == "HIGH" for r in recs)
        focus = "Metabolic & Lipid Optimization" if has_high_priority else "Wellness & Dietary Maintenance"

        return NutritionRecommendationBundle(
            report_id=report_id,
            user_id=user_id,
            recommendations=recs,
            overall_dietary_focus=focus,
        )


nutrition_recommendation_generator = NutritionRecommendationGenerator()
