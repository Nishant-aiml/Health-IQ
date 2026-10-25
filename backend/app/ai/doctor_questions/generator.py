# --------------------------------------------------
# File: generator.py
# Purpose: Pattern-aware doctor discussion question generator.
# Module: AI Engine / Doctor Questions
# Used By: Recommendation Service
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.models import DoctorQuestion, PriorityLevel
from backend.app.ai.doctor_questions.templates import DOCTOR_QUESTION_TEMPLATES


class DoctorQuestionsGenerator:
    """
    Doctor Questions Generator.

    Why it exists:
        Generates pattern-aware, intelligent consultation questions for patients to ask their doctors.
    """

    def generate_questions(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[DoctorQuestion]:
        questions: List[DoctorQuestion] = []

        for p_name, param_info in extracted_parameters.items():
            if param_info.get("severity", "normal") != "normal":
                if p_name in DOCTOR_QUESTION_TEMPLATES:
                    tmpl = DOCTOR_QUESTION_TEMPLATES[p_name]
                    prio = PriorityLevel.HIGH if param_info.get("is_critical") else PriorityLevel.MEDIUM
                    questions.append(
                        DoctorQuestion(
                            question_text=tmpl["question"],
                            target_parameter=p_name,
                            clinical_rationale=tmpl["rationale"],
                            priority=prio,
                        )
                    )

        if not questions:
            questions.append(
                DoctorQuestion(
                    question_text="Are there any preventive lifestyle or dietary adjustments recommended based on my current results?",
                    target_parameter="Overall Baseline",
                    clinical_rationale="Promotes proactive wellness maintenance during routine checkups.",
                    priority=PriorityLevel.LOW,
                )
            )

        return questions


doctor_questions_generator = DoctorQuestionsGenerator()
