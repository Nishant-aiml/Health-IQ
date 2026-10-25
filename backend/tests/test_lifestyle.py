# --------------------------------------------------
# File: test_lifestyle.py
# Purpose: Unit tests for Lifestyle Engine exercise, sleep, hydration, and stress modules.
# Module: Backend Test Suite / Lifestyle Engine
# Used By: Pytest Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

from backend.app.lifestyle.exercise import generate_exercise_recommendations
from backend.app.lifestyle.sleep import generate_sleep_hygiene_plan
from backend.app.lifestyle.hydration import generate_hydration_lifestyle_plan
from backend.app.lifestyle.stress import generate_stress_management_plan


def test_lifestyle_recommendations():
    user = {"age": 45, "gender": "male", "weight_kg": 75.0}
    lab_summary = {"has_high_glucose": True, "has_high_uric_acid": True}

    ex = generate_exercise_recommendations(user, lab_summary)
    assert len(ex) >= 1
    assert "Brisk Walking" in ex[0].activity_name

    sl = generate_sleep_hygiene_plan()
    assert len(sl.habits) == 3

    hy = generate_hydration_lifestyle_plan(user, lab_summary)
    assert hy.daily_volume_liters >= 2.5

    st = generate_stress_management_plan()
    assert "Breathing" in st.technique_name
