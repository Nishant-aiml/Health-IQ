# --------------------------------------------------
# File: test_eli10.py
# Purpose: Unit tests for ELI10 child-friendly explanation generator.
# Module: Backend Test Suite / AI Engine
# Used By: Pytest Execution
# Future Phase: Phase 2C Validation
# --------------------------------------------------

from backend.app.ai.eli10 import eli10_generator


def test_eli10_plain_language_explanation():
    params = {
        "Hemoglobin": {"value": 11.0, "severity": "moderate"},
    }
    explanation = eli10_generator.generate_explanation(params)
    assert "tiny delivery trucks" in explanation.lower() or "oxygen-carrying protein" in explanation.lower()
