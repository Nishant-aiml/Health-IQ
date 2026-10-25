# --------------------------------------------------
# File: hydration.py
# Purpose: Lifestyle Engine hydration plan generator bridging nutrition hydration module.
# Module: Lifestyle Engine / Hydration
# Used By: Lifestyle Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, Any
from backend.app.nutrition.hydration import calculate_personalized_hydration, HydrationGuidanceTarget


def generate_hydration_lifestyle_plan(user_profile: Dict[str, Any], lab_summary: Dict[str, Any]) -> HydrationGuidanceTarget:
    return calculate_personalized_hydration(user_profile, lab_summary)
