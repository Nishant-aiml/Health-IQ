# --------------------------------------------------
# File: generator.py
# Purpose: Generates extended trend-aware recommendations by combining current report analysis with historical trajectories.
# Module: Trend-aware Recommendations / Generator
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from backend.app.history.trends.models import TrendAnalysisResult
from backend.app.history.recommendations.models import TrendRecommendationItem


class TrendRecommendationGenerator:
    """Extends existing recommendations using historical trend context."""

    def generate_trend_recommendations(self, trend_results: List[TrendAnalysisResult]) -> List[TrendRecommendationItem]:
        items: List[TrendRecommendationItem] = []

        for t in trend_results:
            c_name = t.canonical_name
            direction = t.direction

            if direction == "persistent_abnormality":
                items.append(
                    TrendRecommendationItem(
                        canonical_name=c_name,
                        category="Clinical Co-Monitoring",
                        priority="HIGH",
                        trend_context=f"{c_name} has remained persistently outside the reference range across consecutive reports.",
                        actionable_guidance=f"Discuss root-cause evaluation and potential medication or dietary adjustments with your physician.",
                        doctor_question=f"Given that my {c_name} has remained persistently outside reference range across multiple reports, what diagnostic steps do you recommend?",
                        evidence_source="Longitudinal Clinical Care Guidelines",
                    )
                )
            elif direction == "rapid_change":
                items.append(
                    TrendRecommendationItem(
                        canonical_name=c_name,
                        category="Follow-Up Screening",
                        priority="MEDIUM",
                        trend_context=f"A rapid shift of {t.percentage_change}% was observed in {c_name} between recent reports.",
                        actionable_guidance=f"Schedule a repeat laboratory check in 4-6 weeks to confirm whether this shift is transient.",
                        doctor_question=f"Could recent acute changes in lifestyle, medication, or hydration explain this rapid shift in my {c_name}?",
                        evidence_source="Biomarker Volatility Monitoring Guidelines",
                    )
                )
            elif direction == "recovery":
                items.append(
                    TrendRecommendationItem(
                        canonical_name=c_name,
                        category="Health Maintenance",
                        priority="LOW",
                        trend_context=f"{c_name} has successfully recovered into the normal reference range.",
                        actionable_guidance=f"Continue current lifestyle and treatment plan that contributed to this positive recovery.",
                        doctor_question=f"What maintenance strategy should I follow to keep my {c_name} in the healthy reference range?",
                        evidence_source="Preventive Wellness Guidelines",
                    )
                )

        return items


trend_recommendation_generator = TrendRecommendationGenerator()
