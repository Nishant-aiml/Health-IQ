# --------------------------------------------------
# File: recommendation_service.py
# Purpose: Service orchestrator combining Phase 2B report analysis with Phase 2C AI recommendations.
# Module: Recommendation Services
# Used By: Reports API Endpoint Controller
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from sqlmodel import Session
from backend.app.services.report_service import report_service
from backend.app.ai.models import RecommendationBundle
from backend.app.ai.recommendation import recommendation_engine
from backend.app.ai.evidence import evidence_builder
from backend.app.ai.limitations import limitations_generator
from backend.app.ai.doctor_questions import doctor_questions_generator
from backend.app.ai.eli10 import eli10_generator


class RecommendationService:
    """
    Recommendation Service Orchestrator.

    Why it exists:
        Consumes Phase 2B report analysis outputs (health score, parameters, patterns)
        and builds a strongly typed RecommendationBundle containing prioritized recommendations,
        reasoning evidence chains, clinical limitations, doctor questions, and ELI10 explanations.
    """

    def get_recommendations_for_report(self, session: Session, report_id: int) -> RecommendationBundle:
        # Step 1: Consume Phase 2B analysis (Zero recomputation!)
        analysis = report_service.get_report_analysis(session, report_id)

        # Build extracted parameter map
        extracted_param_map = {}
        for p in analysis["parameters"]:
            extracted_param_map[p["canonical_name"]] = {
                "value": p["value"],
                "unit": p["unit"],
                "severity": p["severity"],
                "normal_range_low": p["normal_range_low"],
                "normal_range_high": p["normal_range_high"],
                "is_critical": p.get("is_critical", False),
            }

        detected_patterns = analysis.get("detected_patterns", [])
        has_critical = len(analysis.get("critical_alerts", [])) > 0

        # Step 2: Generate Recommendations (Prioritized)
        recs = recommendation_engine.generate_recommendations(extracted_param_map, detected_patterns)

        # Step 3: Build Evidence Chains
        evidence_chains = evidence_builder.build_evidence_chains(extracted_param_map, detected_patterns, recs)

        # Step 4: Generate Mandatory Clinical Limitations
        limitations = limitations_generator.generate_limitations(has_critical_alerts=has_critical)

        # Step 5: Generate Doctor Discussion Questions
        questions = doctor_questions_generator.generate_questions(extracted_param_map, detected_patterns)

        # Step 6: Generate ELI10 Simple Explanation
        eli10_text = eli10_generator.generate_explanation(extracted_param_map)

        return RecommendationBundle(
            report_id=report_id,
            health_score=analysis["health_score"],
            health_score_summary=analysis["summary"],
            detected_patterns=detected_patterns,
            recommendations=recs,
            evidence_chains=evidence_chains,
            limitations=limitations,
            doctor_questions=questions,
            eli10_explanation=eli10_text,
        )


recommendation_service = RecommendationService()
