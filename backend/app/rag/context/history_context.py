# --------------------------------------------------
# File: history_context.py
# Purpose: Historical RAG context injector incorporating multi-report trends into Grounded Chat.
# Module: RAG Engine / Context Injector
# Used By: Grounded Chat Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.history.trends.models import TrendAnalysisResult
from backend.app.history.change.models import ComparisonResult


def build_historical_rag_context(
    report_count: int,
    trend_results: List[TrendAnalysisResult],
    latest_comparison: Optional[ComparisonResult] = None,
) -> str:
    """Builds structured historical context string for injection into RAG Chat prompt."""
    if report_count <= 1 or not trend_results:
        return "Longitudinal Context: Single report baseline recorded. No multi-report historical trends available."

    lines = [f"Longitudinal Health History ({report_count} Reports Tracked):"]

    for t in trend_results:
        lines.append(
            f"- Biomarker '{t.canonical_name}': Trajectory={t.direction.upper()}, Change={t.percentage_change}%, Confidence={t.trend_confidence}. {t.clinical_summary}"
        )

    if latest_comparison:
        lines.append(f"- Recent Comparative Assessment: {latest_comparison.overall_clinical_assessment}")

    return "\n".join(lines)
