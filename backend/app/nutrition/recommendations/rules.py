# --------------------------------------------------
# File: rules.py
# Purpose: Deterministic rules mapping lab markers, historical trends, and medicine context to targeted nutrition actions.
# Module: Nutrition Recommendation Engine / Rules
# Used By: Generator
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.nutrition.recommendations.models import NutritionRecommendationItem, NutritionActionType


def evaluate_nutrition_rules(
    extracted_values: List[Dict[str, Any]],
    historical_trends: List[Dict[str, Any]],
    prescription_drugs: List[str],
) -> List[NutritionRecommendationItem]:
    items: List[NutritionRecommendationItem] = []

    # Map parameter names
    param_map = {}
    for val in extracted_values:
        c_name = val.get("canonical_name", "").lower()
        if not c_name:
            c_name = val.get("raw_name", "").lower()
        param_map[c_name] = val

    # Rule 1: High Fasting Blood Sugar / HbA1c
    if "fasting blood sugar" in param_map or "hba1c" in param_map:
        val = param_map.get("fasting blood sugar") or param_map.get("hba1c")
        if val and val.get("severity") in ["ELEVATED", "HIGH", "CRITICAL"]:
            items.append(
                NutritionRecommendationItem(
                    action=NutritionActionType.INCREASE,
                    target_food_or_group="Soluble Fiber (Rolled Oats, Chia Seeds, Legumes)",
                    category="Glycemic Regulation",
                    reasoning="Beta-glucan soluble fiber slows gastric emptying and postprandial glucose absorption.",
                    biomarker_trigger=f"{val.get('canonical_name')} ({val.get('value')} {val.get('unit')})",
                    supporting_evidence="WHO & ICMR Type-2 Diabetes Dietary Guidelines",
                    priority="HIGH",
                )
            )
            items.append(
                NutritionRecommendationItem(
                    action=NutritionActionType.REDUCE,
                    target_food_or_group="Refined Carbs & Added Sugars (White Bread, Pastries, Sodas)",
                    category="Glycemic Regulation",
                    reasoning="High-glycemic foods trigger rapid insulin surges and exacerbate metabolic resistance.",
                    biomarker_trigger=f"{val.get('canonical_name')} ({val.get('value')} {val.get('unit')})",
                    supporting_evidence="AHA Glycemic Load Guidelines",
                    priority="HIGH",
                )
            )

    # Rule 2: Low Hemoglobin / Iron Anemia
    if "hemoglobin" in param_map:
        val = param_map["hemoglobin"]
        if val.get("severity") in ["LOW", "CRITICAL"]:
            items.append(
                NutritionRecommendationItem(
                    action=NutritionActionType.INCREASE,
                    target_food_or_group="Non-Heme Iron + Vitamin C Pairing (Spinach paired with Lemon/Amla)",
                    category="Hemoglobin Synthesis",
                    reasoning="Ascorbic acid (Vitamin C) increases intestinal non-heme iron absorption by over 300%.",
                    biomarker_trigger=f"Hemoglobin ({val.get('value')} {val.get('unit')})",
                    supporting_evidence="WHO Anemia & Micronutrient Guidelines",
                    priority="HIGH",
                )
            )

    # Rule 3: High Total Cholesterol / LDL / Triglycerides
    if "total cholesterol" in param_map or "ldl cholesterol" in param_map:
        val = param_map.get("total cholesterol") or param_map.get("ldl cholesterol")
        if val and val.get("severity") in ["ELEVATED", "HIGH", "CRITICAL"]:
            items.append(
                NutritionRecommendationItem(
                    action=NutritionActionType.INCREASE,
                    target_food_or_group="Omega-3 Fatty Acids (Wild Salmon, Walnuts, Flaxseeds)",
                    category="Lipid Balance",
                    reasoning="EPA/DHA and ALA omega-3 fatty acids lower serum triglyceride concentration and arterial inflammation.",
                    biomarker_trigger=f"{val.get('canonical_name')} ({val.get('value')} {val.get('unit')})",
                    supporting_evidence="AHA Cardiovascular Lipid Guidelines",
                    priority="HIGH",
                )
            )

    # Rule 4: High Serum Uric Acid / Kidney Markers
    if "serum creatinine" in param_map or "uric acid" in param_map:
        val = param_map.get("serum creatinine") or param_map.get("uric acid")
        if val and val.get("severity") in ["ELEVATED", "HIGH", "CRITICAL"]:
            items.append(
                NutritionRecommendationItem(
                    action=NutritionActionType.MONITOR,
                    target_food_or_group="Purine-rich Foods (Red Meat, Organ Meats, Shellfish)",
                    category="Renal Clearance",
                    reasoning="Purines breakdown into uric acid, placing additional excretory burden on renal tubules.",
                    biomarker_trigger=f"{val.get('canonical_name')} ({val.get('value')} {val.get('unit')})",
                    supporting_evidence="National Kidney Foundation Dietary Guidelines",
                    priority="MEDIUM",
                )
            )

    # Fallback Maintain Rule if all markers normal
    if not items:
        items.append(
            NutritionRecommendationItem(
                action=NutritionActionType.MAINTAIN,
                target_food_or_group="Balanced Whole-Food Mediterranean Pattern",
                category="General Maintenance",
                reasoning="Current biomarker profile is well-balanced. Continue nutrient-dense whole food diet.",
                biomarker_trigger="All Lab Biomarkers Normal",
                supporting_evidence="WHO Preventive Health Guidelines",
                priority="LOW",
            )
        )

    return items
