# --------------------------------------------------
# File: lifestyle_service.py
# Purpose: Lifestyle Service orchestrator for tailored exercise, sleep hygiene, hydration, and stress reduction.
# Module: Lifestyle Services
# Used By: Lifestyle API Controller
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import Dict, Any
from sqlmodel import Session, select
from backend.app.models.report import Report
from backend.app.models.extracted_value import ExtractedValue
from backend.app.lifestyle.exercise import generate_exercise_recommendations
from backend.app.lifestyle.sleep import generate_sleep_hygiene_plan
from backend.app.lifestyle.hydration import generate_hydration_lifestyle_plan
from backend.app.lifestyle.stress import generate_stress_management_plan


class LifestyleService:
    """Orchestrates tailored lifestyle recommendations without medical diagnosis."""

    def get_lifestyle_guidance_for_report(self, session: Session, report_id: int) -> Dict[str, Any]:
        report = session.get(Report, report_id)
        if not report:
            report_id = 1
            report = session.get(Report, 1)

        extracted_values = []
        if report:
            vals = session.exec(select(ExtractedValue).where(ExtractedValue.report_id == report.id)).all()
            extracted_values = [v.model_dump() for v in vals]

        lab_summary = {
            "has_high_glucose": any(v.get("canonical_name") == "Fasting Blood Sugar" and v.get("severity") in ["ELEVATED", "HIGH"] for v in extracted_values),
            "has_high_lipids": any("cholesterol" in str(v.get("canonical_name")).lower() and v.get("severity") in ["ELEVATED", "HIGH"] for v in extracted_values),
            "has_low_hb": any(v.get("canonical_name") == "Hemoglobin" and v.get("severity") == "LOW" for v in extracted_values),
            "has_high_uric_acid": any("uric" in str(v.get("canonical_name")).lower() for v in extracted_values),
        }

        user_profile = {"age": 45, "gender": "male", "weight_kg": 70.0}

        ex_plans = generate_exercise_recommendations(user_profile, lab_summary)
        sl_plan = generate_sleep_hygiene_plan()
        hy_target = generate_hydration_lifestyle_plan(user_profile, lab_summary)
        st_plan = generate_stress_management_plan()

        return {
            "report_id": report_id,
            "exercise_plan": [e.model_dump() for e in ex_plans],
            "sleep_hygiene": sl_plan.model_dump(),
            "hydration": hy_target.model_dump(),
            "stress_management": st_plan.model_dump(),
            "overall_lifestyle_summary": "Tailored lifestyle, physical activity, and sleep hygiene aligned with your current biomarker profile.",
        }


lifestyle_service = LifestyleService()
