# --------------------------------------------------
# File: test_severity.py
# Purpose: Unit tests for parameter severity evaluation logic.
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2B Validation
# --------------------------------------------------

from backend.app.analysis import evaluate_parameter_severity


def test_severity_normal_in_range():
    assert evaluate_parameter_severity("Hemoglobin", 14.5, 13.8, 17.2) == "normal"
    assert evaluate_parameter_severity("Fasting Blood Sugar", 85.0, 70.0, 99.0) == "normal"


def test_severity_fasting_blood_sugar_tiers():
    assert evaluate_parameter_severity("Fasting Blood Sugar", 110.0, 70.0, 99.0) == "mild"
    assert evaluate_parameter_severity("Fasting Blood Sugar", 150.0, 70.0, 99.0) == "moderate"
    assert evaluate_parameter_severity("Fasting Blood Sugar", 220.0, 70.0, 99.0) == "severe"


def test_severity_percentage_deviations():
    # Mild deviation
    assert evaluate_parameter_severity("Platelet Count", 140.0, 150.0, 450.0) == "mild"
    # Severe deviation
    assert evaluate_parameter_severity("Platelet Count", 50.0, 150.0, 450.0) == "severe"
