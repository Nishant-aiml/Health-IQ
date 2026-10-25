# --------------------------------------------------
# File: test_critical_alerts.py
# Purpose: Unit tests for critical threshold evaluation.
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2B Validation
# --------------------------------------------------

from backend.app.analysis import evaluate_critical_alerts


def test_critical_alert_triggers():
    # Fasting Blood Sugar > 300 mg/dL
    alerts = evaluate_critical_alerts([{"canonical_name": "Fasting Blood Sugar", "value": 340.0, "unit": "mg/dL"}])
    assert len(alerts) == 1
    assert alerts[0]["is_critical"] is True
    assert alerts[0]["parameter_name"] == "Fasting Blood Sugar"

    # Hemoglobin < 7.0 g/dL
    alerts = evaluate_critical_alerts([{"canonical_name": "Hemoglobin", "value": 6.2, "unit": "g/dL"}])
    assert len(alerts) == 1
    assert alerts[0]["parameter_name"] == "Hemoglobin"


def test_multiple_critical_alerts():
    items = [
        {"canonical_name": "Fasting Blood Sugar", "value": 350.0, "unit": "mg/dL"},
        {"canonical_name": "Hemoglobin", "value": 5.8, "unit": "g/dL"},
        {"canonical_name": "Platelet Count", "value": 30.0, "unit": "x10^3/uL"},
    ]
    alerts = evaluate_critical_alerts(items)
    assert len(alerts) == 3
