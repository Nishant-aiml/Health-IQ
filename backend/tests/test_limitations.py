# --------------------------------------------------
# File: test_limitations.py
# Purpose: Unit tests for mandatory limitation inclusion.
# Module: Backend Test Suite / AI Engine
# Used By: Pytest Execution
# Future Phase: Phase 2C Validation
# --------------------------------------------------

from backend.app.ai.limitations import limitations_generator


def test_limitations_mandatory_inclusion():
    limits = limitations_generator.generate_limitations(has_critical_alerts=False)
    assert len(limits) >= 3
    assert any("non-diagnostic" in lim.notice.lower() for lim in limits)


def test_limitations_critical_alert_addition():
    limits = limitations_generator.generate_limitations(has_critical_alerts=True)
    assert len(limits) >= 4
    assert any("critical medical values" in lim.notice.lower() for lim in limits)
