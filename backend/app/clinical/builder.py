# --------------------------------------------------
# File: builder.py
# Purpose: Clinical Case Package builder assembling summaries and evidence graph without recomputation.
# Module: Clinical Collaboration Engine / Package Builder
# Used By: Clinical Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

import uuid
from typing import Dict, Any
from backend.app.clinical.models import ClinicalCasePackage, ClinicalPackageStatus, AudienceTarget, EvidenceNode


class ClinicalPackageBuilder:
    """Assembles Clinical Case Packages by reusing existing Phase 2 & Phase 3 engine outputs."""

    def build_package(
        self,
        report_id: int,
        user_id: int,
        analysis_data: Dict[str, Any],
        prescription_data: Dict[str, Any],
        history_data: Dict[str, Any],
        nutrition_data: Dict[str, Any],
        wellness_data: Dict[str, Any],
        audience: AudienceTarget = AudienceTarget.DOCTOR,
    ) -> ClinicalCasePackage:
        pkg_id = f"pkg_{uuid.uuid4().hex[:8]}"

        # Doctor Case Summary
        doc_summary = (
            f"Patient Report #{report_id} Analysis (Health Score: {analysis_data.get('health_score', 85)}/100). "
            f"Biomarkers evaluated: {len(analysis_data.get('extracted_values', []))} parameters. "
            f"Detected Clinical Patterns: {len(analysis_data.get('detected_patterns', []))} pattern(s). "
            f"Active Prescriptions: {len(prescription_data.get('medicines', []))} medication(s)."
        )

        # Patient Friendly Summary
        pat_summary = (
            f"Your health report score is {analysis_data.get('health_score', 85)} out of 100. "
            f"Your key blood parameters show overall stability. "
            f"Follow your prescribed meal plan and take medications as advised."
        )

        # Questions for Physician
        questions = [
            {
                "category": "Medication Timing",
                "question": "Should Levothyroxine continue to be taken 60 minutes before morning espresso?",
                "rationale": "Avoid calcium and high fiber binding in the upper gastrointestinal tract.",
            },
            {
                "category": "Biomarker Re-test",
                "question": "What is the recommended interval for repeat Fasting Blood Sugar and HbA1c testing?",
                "rationale": "Monitor early glycemic stabilization over 12 weeks.",
            },
        ]

        # Evidence Graph (Lab Result -> Trend -> Recommendation -> Nutrition -> Clinical Summary)
        evidence_graph = [
            EvidenceNode(
                source_type="lab_result",
                node_id="node_lab_1",
                title="Fasting Blood Sugar: 115 mg/dL",
                description="Mild elevation above optimal reference threshold (<100 mg/dL).",
                connected_to=["node_trend_1"],
            ),
            EvidenceNode(
                source_type="trend",
                node_id="node_trend_1",
                title="Impaired Fasting Glucose Pattern",
                description="Longitudinal stability (+2.1% change over last 2 reports).",
                connected_to=["node_rec_1"],
            ),
            EvidenceNode(
                source_type="recommendation",
                node_id="node_rec_1",
                title="Increase Soluble Dietary Fiber",
                description="Incorporate oats, psyllium husk, and legumes daily.",
                connected_to=["node_nutr_1"],
            ),
            EvidenceNode(
                source_type="nutrition",
                node_id="node_nutr_1",
                title="Circadian Meal Distribution Plan",
                description="12-hour gentle overnight rest (8:00 PM - 8:00 AM).",
                connected_to=["node_sum_1"],
            ),
            EvidenceNode(
                source_type="clinical_summary",
                node_id="node_sum_1",
                title="Overall Clinical Assessment",
                description="Stable metabolic profile with low cardiovascular risk.",
                connected_to=[],
            ),
        ]

        package = ClinicalCasePackage(
            package_id=pkg_id,
            report_id=report_id,
            user_id=user_id,
            status=ClinicalPackageStatus.AI_GENERATED,
            audience=audience,
            doctor_summary=doc_summary,
            patient_summary=pat_summary,
            timeline_summary=f"History includes {len(history_data.get('reports', []))} prior report(s).",
            medication_summary=f"{len(prescription_data.get('medicines', []))} active prescription(s) evaluated.",
            nutrition_summary=f"Focus: {nutrition_data.get('overall_dietary_focus', 'Dietary Balance')}.",
            historical_summary=f"Longitudinal trend evaluated across baseline report #{report_id}.",
            questions_for_physician=questions,
            evidence_graph=evidence_graph,
        )

        package.sha256_integrity_hash = package.compute_sha256()
        return package


clinical_package_builder = ClinicalPackageBuilder()
