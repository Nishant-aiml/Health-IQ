# --------------------------------------------------
# File: stress.py
# Purpose: Stress reduction techniques, autonomic nervous system regulation, and physiological recovery advice.
# Module: Lifestyle Engine / Stress
# Used By: Lifestyle Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.lifestyle.models import StressManagementPlan


def generate_stress_management_plan() -> StressManagementPlan:
    return StressManagementPlan(
        technique_name="4-7-8 Diaphragmatic Breathing & Physiological Sigh",
        practice_frequency="2 Sessions / Day (5 minutes each)",
        autonomic_mechanism="Prolonged exhalation stimulates vagal nerve activity, triggering parasympathetic cholinergic slowing of heart rate.",
        recovery_guidance="Practice upon waking and prior to bedtime to lower baseline sympathetic tone and salivary cortisol levels.",
    )
