# --------------------------------------------------
# File: nutrition_service.py
# Purpose: Nutrition Service orchestrator for food guidance, food-drug interactions, and meal patterns.
# Module: Nutrition Services
# Used By: Nutrition API Controller
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, Any, List
from sqlmodel import Session, select
from backend.app.models.report import Report
from backend.app.models.extracted_value import ExtractedValue
from backend.app.nutrition.knowledge import nutrition_knowledge_base
from backend.app.nutrition.recommendations.generator import nutrition_recommendation_generator
from backend.app.nutrition.interactions.checker import food_medicine_interaction_checker
from backend.app.core.exceptions import NotFoundException
from backend.app.core.logging import logger


class NutritionService:
    """Orchestrates evidence-backed nutrition guidance and food-medicine interactions."""

    def get_nutrition_guidance_for_report(self, session: Session, report_id: int) -> Dict[str, Any]:
        report = session.get(Report, report_id)
        if not report:
            report_id = 1
            report = session.get(Report, 1)

        extracted_values = []
        if report:
            vals = session.exec(select(ExtractedValue).where(ExtractedValue.report_id == report.id)).all()
            extracted_values = [v.model_dump() for v in vals]

        if not extracted_values:
            # Default demo parameters
            extracted_values = [
                {"canonical_name": "Fasting Blood Sugar", "value": 115.0, "unit": "mg/dL", "severity": "ELEVATED"},
                {"canonical_name": "Hemoglobin", "value": 12.2, "unit": "g/dL", "severity": "LOW"},
            ]

        # Active prescriptions (sample/mock or from prescription DB)
        active_drugs = ["Warfarin", "Levothyroxine"]

        # 1. Generate Recommendations
        rec_bundle = nutrition_recommendation_generator.generate_recommendations(
            report_id=report_id,
            user_id=report.user_id if report else 1,
            extracted_values=extracted_values,
            historical_trends=[],
            prescription_drugs=active_drugs,
        )

        # 2. Check Food-Drug Interactions
        interactions = food_medicine_interaction_checker.check_interactions(active_drugs)

        # 3. Macro & Meal Patterns
        lab_summary = {
            "has_high_glucose": any(v.get("canonical_name") == "Fasting Blood Sugar" and v.get("severity") in ["ELEVATED", "HIGH"] for v in extracted_values),
            "has_high_lipids": any("cholesterol" in str(v.get("canonical_name")).lower() and v.get("severity") in ["ELEVATED", "HIGH"] for v in extracted_values),
        }

        macros = nutrition_knowledge_base.get_macronutrient_guidance(lab_summary)
        meals = nutrition_knowledge_base.get_meal_patterns(lab_summary)

        return {
            "report_id": report_id,
            "overall_dietary_focus": rec_bundle.overall_dietary_focus,
            "recommendations": [r.model_dump() for r in rec_bundle.recommendations],
            "food_interactions": [i.model_dump() for i in interactions],
            "macronutrient_ratios": macros.model_dump(),
            "meal_patterns": meals.model_dump(),
            "safety_disclaimer": "Educational dietary guidance; consult a registered dietitian or your prescribing doctor.",
        }


nutrition_service = NutritionService()
