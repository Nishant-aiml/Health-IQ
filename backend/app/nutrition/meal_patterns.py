# --------------------------------------------------
# File: meal_patterns.py
# Purpose: Circadian meal timing, meal distribution, and healthy eating window guidance.
# Module: Nutrition Knowledge Engine / Meal Patterns
# Used By: Knowledge Base & Recommendation Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from pydantic import BaseModel, Field


class MealScheduleItem(BaseModel):
    meal_name: str
    recommended_time_window: str
    macronutrient_focus: str
    circadian_rationale: str


class CircadianMealGuidance(BaseModel):
    overnight_fasting_window: str = "12-14 Hours (Circadian Alignment)"
    meals: List[MealScheduleItem] = Field(default_factory=list)
    key_principle: str = "Front-load caloric intake earlier in the day when insulin sensitivity peak is highest."


def generate_circadian_meal_patterns(lab_summary: Dict[str, Any]) -> CircadianMealGuidance:
    """Generates circadian meal timing guidance based on metabolic lab markers."""
    has_high_glucose = lab_summary.get("has_high_glucose", False)

    meals = [
        MealScheduleItem(
            meal_name="Breakfast / Morning Meal",
            recommended_time_window="7:30 AM - 9:00 AM (Within 90 mins of waking)",
            macronutrient_focus="High Protein (25-30g) + Soluble Fiber + Healthy Fats",
            circadian_rationale="Optimizes morning cortisol awakening response (CAR) and buffers glucose excursion.",
        ),
        MealScheduleItem(
            meal_name="Mid-Day Lunch",
            recommended_time_window="12:30 PM - 2:00 PM",
            macronutrient_focus="Complex Carbs + Lean Protein + Phytonutrient Vegetables",
            circadian_rationale="Aligns with peak digestive enzyme secretion and core body temperature zenith.",
        ),
        MealScheduleItem(
            meal_name="Evening Dinner",
            recommended_time_window="6:30 PM - 8:00 PM (At least 3 hours before sleep)",
            macronutrient_focus="Light Fiber + Tryptophan-rich Protein (e.g. Salmon/Tofu)",
            circadian_rationale="Prevents late-night melatonin-driven glucose intolerance and promotes restorative slow-wave sleep.",
        ),
    ]

    note = (
        "Focus on consistent 12-hour overnight rest (e.g. 8 PM to 8 AM) to support hepatic glycogen depletion. "
        "Avoid extreme caloric restriction or prolonged starvation protocols."
    )
    if has_high_glucose:
        note += " Avoid high-glycemic carbohydrates after 7 PM."

    return CircadianMealGuidance(
        overnight_fasting_window="12 Hours Gentle Circadian Rest",
        meals=meals,
        key_principle=note,
    )
