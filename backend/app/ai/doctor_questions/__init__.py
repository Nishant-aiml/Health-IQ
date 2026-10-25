# --------------------------------------------------
# File: __init__.py
# Purpose: Doctor Questions package index.
# Module: AI Engine / Doctor Questions
# Used By: Recommendation Service
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.doctor_questions.generator import DoctorQuestionsGenerator, doctor_questions_generator

__all__ = [
    "DoctorQuestionsGenerator",
    "doctor_questions_generator",
]
