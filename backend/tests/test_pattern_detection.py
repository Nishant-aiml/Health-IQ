# --------------------------------------------------
# File: test_pattern_detection.py
# Purpose: Unit tests for rule-based clinical pattern detection.
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2B Validation
# --------------------------------------------------

from backend.app.analysis import pattern_registry


def test_microcytic_anemia_pattern():
    params = {
        "Hemoglobin": {"value": 10.2, "normal_range_low": 13.8},
        "Mean Corpuscular Volume": {"value": 72.0, "normal_range_low": 80.0},
    }
    patterns = pattern_registry.evaluate_all(params)
    assert len(patterns) == 1
    assert patterns[0]["pattern_name"] == "Microcytic Anemia Pattern"
    assert "Hemoglobin" in patterns[0]["triggered_by"]


def test_metabolic_syndrome_pattern():
    params = {
        "Fasting Blood Sugar": {"value": 140.0, "normal_range_high": 99.0},
        "Triglycerides": {"value": 190.0, "normal_range_high": 149.0},
    }
    patterns = pattern_registry.evaluate_all(params)
    assert len(patterns) == 1
    assert patterns[0]["pattern_name"] == "Metabolic Syndrome Risk Pattern"
