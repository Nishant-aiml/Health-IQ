# --------------------------------------------------
# File: test_doctor_questions.py
# Purpose: Unit tests for doctor discussion question generation.
# Module: Backend Test Suite / AI Engine
# Used By: Pytest Execution
# Future Phase: Phase 2C Validation
# --------------------------------------------------

from backend.app.ai.doctor_questions import doctor_questions_generator


def test_doctor_questions_generation():
    params = {
        "Fasting Blood Sugar": {"value": 140.0, "severity": "moderate", "is_critical": False},
    }
    questions = doctor_questions_generator.generate_questions(params, [])
    assert len(questions) == 1
    assert "HbA1c" in questions[0].question_text
    assert questions[0].target_parameter == "Fasting Blood Sugar"
