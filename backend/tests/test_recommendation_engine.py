# --------------------------------------------------
# File: test_recommendation_engine.py
# Purpose: Unit tests for recommendation generation, priority sorting, and rule execution.
# Module: Backend Test Suite / AI Engine
# Used By: Pytest Execution
# Future Phase: Phase 2C Validation
# --------------------------------------------------

from backend.app.ai.recommendation import recommendation_engine
from backend.app.ai.models import PriorityLevel


def test_recommendation_priority_sorting():
    params = {
        "Hemoglobin": {"value": 6.5, "severity": "severe", "is_critical": True, "normal_range_low": 13.8},
        "Total Cholesterol": {"value": 220.0, "severity": "mild", "is_critical": False, "normal_range_high": 199.0},
    }
    recs = recommendation_engine.generate_recommendations(params, [])

    assert len(recs) >= 2
    # Critical recommendation (Anemia) must come before Medium recommendation (Lipid)
    assert recs[0].priority == PriorityLevel.CRITICAL
    assert recs[0].recommendation_id == "ANEMIA_LOW_HB"


def test_recommendation_optimal_fallback():
    # When all parameters are normal, return informational baseline recommendation
    params = {}
    recs = recommendation_engine.generate_recommendations(params, [])
    assert len(recs) == 1
    assert recs[0].recommendation_id == "HEALTH_OPTIMAL_BASELINE"
    assert recs[0].priority == PriorityLevel.INFORMATIONAL
