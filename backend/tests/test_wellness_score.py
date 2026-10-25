# --------------------------------------------------
# File: test_wellness_score.py
# Purpose: Unit tests for Wellness Score Engine transparent weighting and Health Score reuse.
# Module: Backend Test Suite / Wellness Score Engine
# Used By: Pytest Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

from backend.app.wellness.calculator import wellness_score_calculator
from backend.app.wellness.weights import compute_composite_wellness_score


def test_wellness_score_calculation():
    reused_health_score = 80.0

    breakdown = wellness_score_calculator.calculate_wellness(
        report_id=1,
        user_id=1,
        reused_health_score=reused_health_score,
        abnormal_count=1,
        critical_count=0,
    )

    assert breakdown.health_score_reused == 80.0
    assert 0 <= breakdown.overall_wellness_score <= 100
    assert "Health Score baseline (80.0 × 40%)" in breakdown.formula_explanation


def test_weighted_formula():
    score = compute_composite_wellness_score(100.0, 100.0, 100.0, 100.0, 100.0)
    assert score == 100.0
