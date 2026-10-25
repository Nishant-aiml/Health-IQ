# --------------------------------------------------
# File: calculator.py
# Purpose: Wellness Score Calculator deriving domain scores while REUSING Phase 2B Health Score baseline.
# Module: Wellness Score Engine / Calculator
# Used By: Wellness Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, Any, List
from backend.app.wellness.models import WellnessScoreBreakdown
from backend.app.wellness.weights import compute_composite_wellness_score


class WellnessScoreCalculator:
    """Calculates domain wellness scores (Nutrition, Lifestyle, Hydration, Sleep) and overall score."""

    def calculate_wellness(
        self,
        report_id: int,
        user_id: int,
        reused_health_score: float,
        abnormal_count: int,
        critical_count: int,
    ) -> WellnessScoreBreakdown:
        # Base penalties from abnormal/critical markers
        penalty = (abnormal_count * 5.0) + (critical_count * 15.0)

        nutrition = round(max(50.0, 95.0 - penalty), 1)
        lifestyle = round(max(60.0, 90.0 - (penalty * 0.8)), 1)
        hydration = round(max(70.0, 92.0 - (penalty * 0.5)), 1)
        sleep = round(max(65.0, 88.0 - (penalty * 0.6)), 1)

        overall = compute_composite_wellness_score(
            health_score=reused_health_score,
            nutrition_score=nutrition,
            lifestyle_score=lifestyle,
            hydration_score=hydration,
            sleep_score=sleep,
        )

        return WellnessScoreBreakdown(
            report_id=report_id,
            user_id=user_id,
            health_score_reused=reused_health_score,
            nutrition_score=nutrition,
            lifestyle_score=lifestyle,
            hydration_score=hydration,
            sleep_score=sleep,
            overall_wellness_score=overall,
            formula_explanation=(
                f"Overall Wellness ({overall}/100) calculated transparently: "
                f"Health Score baseline ({reused_health_score} × 40%) + Nutrition ({nutrition} × 25%) + "
                f"Lifestyle ({lifestyle} × 15%) + Hydration ({hydration} × 10%) + Sleep ({sleep} × 10%)."
            ),
        )


wellness_score_calculator = WellnessScoreCalculator()
