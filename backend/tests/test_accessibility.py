# --------------------------------------------------
# File: test_accessibility.py
# Purpose: Unit tests for Accessibility Engine profile settings and medical term simplifier.
# Module: Backend Test Suite / Accessibility Engine
# Used By: Pytest Execution
# Future Phase: Phase 3D Validation
# --------------------------------------------------

from backend.app.accessibility.simplifier import medical_term_simplifier
from backend.app.accessibility.models import AccessibilityProfileType


def test_accessibility_simplifier_senior():
    text = "Postprandial glucose excursion requires monitoring."
    simplified = medical_term_simplifier.simplify_text(text, AccessibilityProfileType.SENIOR)

    assert "after meal" in simplified.lower()
    assert "blood sugar jump after eating" in simplified.lower()
