# --------------------------------------------------
# File: generator.py
# Purpose: Longitudinal Summary Generator orchestrator compiling clinical summaries, ELI10 notes, and disclaimers.
# Module: Longitudinal Summary Generator / Generator
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.history.trends.models import TrendAnalysisResult
from backend.app.history.summary.templates import LONGITUDINAL_SUMMARY_TEMPLATE, LONGITUDINAL_DISCLAIMER
from backend.app.history.summary.eli10 import generate_trend_eli10


class LongitudinalSummaryGenerator:
    """Compiles multi-report trend summaries and ELI10 analogies."""

    def generate_summary(
        self,
        report_count: int,
        initial_score: float,
        latest_score: float,
        trend_results: List[TrendAnalysisResult],
    ) -> Dict[str, Any]:
        score_delta = round(latest_score - initial_score, 1)

        trends_lines = []
        improved_cnt = 0
        stable_cnt = 0
        attention_cnt = 0

        eli10_notes = []

        for t in trend_results:
            trends_lines.append(f"- {t.canonical_name}: {t.direction.upper()} ({t.percentage_change}%)")
            eli_note = generate_trend_eli10(t.canonical_name, t.direction, t.percentage_change)
            eli10_notes.append(eli_note)

            if t.direction == "recovery":
                improved_cnt += 1
            elif t.direction in ["persistent_abnormality", "rapid_change"]:
                attention_cnt += 1
            else:
                stable_cnt += 1

        summary_text = LONGITUDINAL_SUMMARY_TEMPLATE.format(
            report_count=report_count,
            initial_score=initial_score,
            latest_score=latest_score,
            score_delta=f"+{score_delta}" if score_delta > 0 else str(score_delta),
            trends_summary="\n".join(trends_lines) if trends_lines else "- No trend data available",
            improved_count=improved_cnt,
            stable_count=stable_cnt,
            attention_count=attention_cnt,
        ).strip()

        return {
            "summary_text": summary_text,
            "eli10_notes": eli10_notes,
            "disclaimer": LONGITUDINAL_DISCLAIMER,
        }


longitudinal_summary_generator = LongitudinalSummaryGenerator()
