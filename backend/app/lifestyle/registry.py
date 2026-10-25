# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Lifestyle Engine.
# Module: Lifestyle Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.lifestyle.exercise import generate_exercise_recommendations
from backend.app.lifestyle.sleep import generate_sleep_hygiene_plan
from backend.app.lifestyle.hydration import generate_hydration_lifestyle_plan
from backend.app.lifestyle.stress import generate_stress_management_plan


class LifestyleRegistry:
    def get_lifestyle_bundle(self, user_profile, lab_summary):
        ex = generate_exercise_recommendations(user_profile, lab_summary)
        sl = generate_sleep_hygiene_plan()
        hy = generate_hydration_lifestyle_plan(user_profile, lab_summary)
        st = generate_stress_management_plan()
        return {
            "exercise": ex,
            "sleep": sl,
            "hydration": hy,
            "stress": st,
        }


lifestyle_registry = LifestyleRegistry()
