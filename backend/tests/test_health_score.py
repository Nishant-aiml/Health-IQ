# --------------------------------------------------
# File: test_health_score.py
# Purpose: Unit tests for explainable Health Score computation (0-100).
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2B Validation
# --------------------------------------------------

from backend.app.analysis import calculate_health_score


def test_health_score_all_normal():
    items = [
        {"canonical_name": "Hemoglobin", "severity": "normal", "is_critical": False},
        {"canonical_name": "Fasting Blood Sugar", "severity": "normal", "is_critical": False},
    ]
    res = calculate_health_score(items)
    assert res["score"] == 100
    assert len(res["penalties_breakdown"]) == 0


def test_health_score_penalties_and_clamping():
    items = [
        {"canonical_name": "Hemoglobin", "severity": "mild", "is_critical": False},        # -5
        {"canonical_name": "Fasting Blood Sugar", "severity": "moderate", "is_critical": False}, # -12
    ]
    res = calculate_health_score(items)
    assert res["score"] == 83
    assert len(res["penalties_breakdown"]) == 2
    assert res["penalties_breakdown"][0]["points_deducted"] == 5
    assert res["penalties_breakdown"][1]["points_deducted"] == 12


def test_health_score_clamped_to_zero():
    # Multiple critical penalties
    items = [
        {"canonical_name": "Hemoglobin", "severity": "critical", "is_critical": True}, # -35
        {"canonical_name": "Platelets", "severity": "critical", "is_critical": True},  # -35
        {"canonical_name": "Sugar", "severity": "critical", "is_critical": True},      # -35
    ]
    res = calculate_health_score(items)
    assert res["score"] == 0
