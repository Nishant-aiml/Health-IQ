# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Wellness Score Engine.
# Module: Wellness Score Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.wellness.calculator import wellness_score_calculator, WellnessScoreCalculator


class WellnessRegistry:
    def calculate_wellness(self, report_id, user_id, reused_health_score, abnormal_count, critical_count):
        return wellness_score_calculator.calculate_wellness(
            report_id, user_id, reused_health_score, abnormal_count, critical_count
        )


wellness_registry = WellnessRegistry()
