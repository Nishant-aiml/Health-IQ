# --------------------------------------------------
# File: exercise.py
# Purpose: Generates tailored physical activity and aerobic exercise suggestions adjusted for lab markers.
# Module: Lifestyle Engine / Exercise
# Used By: Lifestyle Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.lifestyle.models import ExercisePlan


def generate_exercise_recommendations(user_profile: Dict[str, Any], lab_summary: Dict[str, Any]) -> List[ExercisePlan]:
    plans: List[ExercisePlan] = []

    has_high_glucose = lab_summary.get("has_high_glucose", False)
    has_high_lipids = lab_summary.get("has_high_lipids", False)
    has_low_hb = lab_summary.get("has_low_hb", False)

    if has_low_hb:
        plans.append(
            ExercisePlan(
                activity_name="Low-Impact Zone 1 Walking & Gentle Yoga",
                frequency_weekly="4 - 5 Days / Week",
                duration_minutes_per_session=25,
                intensity_level="Light (RPE 3-4)",
                physiological_rationale="Promotes peripheral blood circulation without stressing reduced oxygen-carrying hemoglobin capacity.",
                safety_precautions="Rest immediately if experiencing dizziness, lightheadedness, or shortness of breath.",
            )
        )
    elif has_high_glucose:
        plans.append(
            ExercisePlan(
                activity_name="Brisk Walking & Post-Meal Glucose Walks",
                frequency_weekly="5 - 6 Days / Week",
                duration_minutes_per_session=30,
                intensity_level="Moderate Zone 2 (RPE 5-6)",
                physiological_rationale="Stimulates GLUT4 glucose transporter translocation independent of insulin, lowering postprandial glucose.",
                safety_precautions="Take a 10-15 minute walk within 30 minutes after major meals.",
            )
        )
        plans.append(
            ExercisePlan(
                activity_name="Light Resistance / Bodyweight Strength Exercises",
                frequency_weekly="3 Days / Week",
                duration_minutes_per_session=20,
                intensity_level="Moderate",
                physiological_rationale="Increases skeletal muscle mass, the primary sink for peripheral glucose disposition.",
                safety_precautions="Maintain proper breathing technique; avoid Valsalva maneuver if blood pressure is elevated.",
            )
        )
    elif has_high_lipids:
        plans.append(
            ExercisePlan(
                activity_name="Sustained Aerobic Cycling / Swimming",
                frequency_weekly="4 - 5 Days / Week",
                duration_minutes_per_session=40,
                intensity_level="Moderate Zone 2",
                physiological_rationale="Enhances lipoprotein lipase (LPL) activity, accelerating triglyceride clearance and elevating HDL.",
                safety_precautions="Warm up for 5 minutes prior to sustained aerobic exertion.",
            )
        )
    else:
        plans.append(
            ExercisePlan(
                activity_name="Brisk Walking & Functional Aerobics",
                frequency_weekly="5 Days / Week",
                duration_minutes_per_session=30,
                intensity_level="Moderate Zone 2",
                physiological_rationale="Maintains cardiovascular conditioning, endothelial nitric oxide synthesis, and insulin sensitivity.",
                safety_precautions="Stay hydrated before and during exercise.",
            )
        )

    return plans
