# --------------------------------------------------
# File: nutrients.py
# Purpose: Micronutrient and Macronutrient definitions, biological roles, and linked lab markers.
# Module: Nutrition Knowledge Engine / Nutrients
# Used By: Knowledge Base & Recommendation Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, List, Any
from backend.app.nutrition.models import MicronutrientInfo, MacronutrientRatio

MICRONUTRIENT_DATABASE: Dict[str, MicronutrientInfo] = {
    "Iron": MicronutrientInfo(
        name="Iron (Fe)",
        biological_role="Essential component of hemoglobin oxygen transport and cytochrome oxidative enzymes.",
        dietary_sources=["Spinach", "Lentils", "Pumpkin Seeds", "Lean Poultry", "Amla with Citrus"],
        deficiency_signs=["Fatigue", "Pale conjunctiva", "Shortness of breath on exertion", "Brittle nails"],
        lab_markers_linked=["Hemoglobin", "Serum Ferritin", "Total Iron Binding Capacity"],
    ),
    "Vitamin D": MicronutrientInfo(
        name="Vitamin D (Calcitriol)",
        biological_role="Regulates calcium and phosphate absorption, osteoblast mineralization, and T-cell immune modulation.",
        dietary_sources=["Sunlight Exposure", "Wild Salmon", "Egg Yolks", "Fortified Dairy/Plant Milk"],
        deficiency_signs=["Bone pain", "Muscle weakness", "Frequent infections", "Low mood"],
        lab_markers_linked=["Vitamin D 25-OH", "Serum Calcium", "Alkaline Phosphatase"],
    ),
    "Vitamin B12": MicronutrientInfo(
        name="Vitamin B12 (Cobalamin)",
        biological_role="Required for myelin sheath maintenance, DNA synthesis, and red blood cell maturation.",
        dietary_sources=["Fortified Cereals", "Eggs", "Dairy", "Nutritional Yeast", "Fish"],
        deficiency_signs=["Peripheral neuropathy (tingling in fingers/toes)", "Glossitis", "Macrocytic anemia"],
        lab_markers_linked=["Serum Vitamin B12", "Homocysteine", "Mean Corpuscular Volume (MCV)"],
    ),
    "Potassium": MicronutrientInfo(
        name="Potassium (K+)",
        biological_role="Primary intracellular electrolyte maintaining resting membrane potential and vascular tone.",
        dietary_sources=["Coconut Water", "Bananas", "Spinach", "Sweet Potatoes", "Avocados"],
        deficiency_signs=["Muscle cramps", "Cardiac palpitations", "Elevated blood pressure"],
        lab_markers_linked=["Serum Potassium", "Systolic Blood Pressure", "Diastolic Blood Pressure"],
    ),
}


def get_recommended_macronutrient_ratio(lab_summary: Dict[str, Any]) -> MacronutrientRatio:
    """Computes targeted macro distribution based on lab markers (e.g. Glucose, Lipid Profile)."""
    has_high_glucose = lab_summary.get("has_high_glucose", False)
    has_high_lipids = lab_summary.get("has_high_lipids", False)

    if has_high_glucose:
        return MacronutrientRatio(
            carbohydrates_pct=40.0,
            protein_pct=30.0,
            fats_pct=30.0,
            fiber_grams_daily=38.0,
            guidance_note="Controlled carbohydrate ratio with high soluble fiber to buffer postprandial glucose spikes.",
        )
    elif has_high_lipids:
        return MacronutrientRatio(
            carbohydrates_pct=45.0,
            protein_pct=25.0,
            fats_pct=30.0,
            fiber_grams_daily=35.0,
            guidance_note="Emphasizes monounsaturated healthy fats (MUFA/PUFA) and plant sterols to lower circulating ApoB/LDL.",
        )

    return MacronutrientRatio(
        carbohydrates_pct=50.0,
        protein_pct=25.0,
        fats_pct=25.0,
        fiber_grams_daily=30.0,
        guidance_note="Balanced Mediterranean-style macronutrient distribution supporting long-term metabolic health.",
    )
