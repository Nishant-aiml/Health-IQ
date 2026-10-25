# --------------------------------------------------
# File: hydration.py
# Purpose: Calculates personalized daily fluid intake targets, fluid pacing, and hydration indicators.
# Module: Nutrition Knowledge Engine / Hydration
# Used By: Knowledge Base & Lifestyle Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, Any
from pydantic import BaseModel, Field


class HydrationGuidanceTarget(BaseModel):
    daily_volume_liters: float
    daily_glasses_count: int
    pacing_guideline: str
    urine_color_target: str = "Pale Straw / Light Yellow (Chart #1-#2)"
    electrolyte_advice: str
    clinical_note: str


def calculate_personalized_hydration(user_profile: Dict[str, Any], lab_summary: Dict[str, Any]) -> HydrationGuidanceTarget:
    """Calculates daily fluid target based on baseline weight (~35 ml/kg) and lab markers."""
    age = user_profile.get("age", 40)
    gender = user_profile.get("gender", "male")
    weight_kg = user_profile.get("weight_kg", 70.0)

    # Base formula: 35 ml per kg body weight
    base_ml = weight_kg * 35.0
    base_liters = round(base_ml / 1000.0, 1)

    # Adjust for lab renal markers
    creatinine_high = lab_summary.get("has_high_creatinine", False)
    uric_acid_high = lab_summary.get("has_high_uric_acid", False)

    note = "Calculated from baseline physiological water turnover rates (~35 mL/kg/day)."
    electrolyte_advice = "Incorporate plain water, herbal teas, and coconut water. Avoid sugary electrolyte sodas."

    if uric_acid_high or creatinine_high:
        base_liters = max(2.8, base_liters + 0.5)
        note += " Hydration target increased (+500 mL) to support renal clearance of serum uric acid and nitrogenous waste."
        electrolyte_advice += " Maintain consistent fluid intake throughout waking hours to prevent urinary crystal precipitation."

    glasses = int(round(base_liters * 4.0)) # 1 glass ~250 ml

    return HydrationGuidanceTarget(
        daily_volume_liters=base_liters,
        daily_glasses_count=glasses,
        pacing_guideline="Drink 1 glass (250 mL) upon waking, then pace 1 glass every 90-120 minutes until 2 hours before sleep.",
        urine_color_target="Pale Straw / Transparent Yellow",
        electrolyte_advice=electrolyte_advice,
        clinical_note=note,
    )
