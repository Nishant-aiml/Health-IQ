# --------------------------------------------------
# File: analyzer.py
# Purpose: Clinical Change Engine orchestrator building ComparisonResult across report pairs.
# Module: Clinical Change Engine / Analyzer
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.change.models import ComparisonResult, BiomarkerChangeItem, ComparisonMode
from backend.app.history.change.comparator import clinical_comparator


class ChangeAnalyzer:
    """Orchestrates comparative report analysis."""

    def compare_reports(
        self,
        mode: ComparisonMode,
        target_report_id: int,
        reference_report_id: int,
        target_readings: List[HistoricalParameterReading],
        reference_readings: List[HistoricalParameterReading],
        target_score: float = 100.0,
        reference_score: float = 100.0,
    ) -> ComparisonResult:
        ref_dict = {r.canonical_name: r for r in reference_readings}
        changes: List[BiomarkerChangeItem] = []

        improved = 0
        unchanged = 0
        worsened = 0

        for t_reading in target_readings:
            c_name = t_reading.canonical_name
            if c_name in ref_dict:
                r_reading = ref_dict[c_name]
                item = clinical_comparator.compare_readings(c_name, t_reading, r_reading)
                changes.append(item)

                if item.change_status == "Improved":
                    improved += 1
                elif item.change_status == "Worsened":
                    worsened += 1
                else:
                    unchanged += 1

        score_delta = round(target_score - reference_score, 1)

        t_date = target_readings[0].collection_date if target_readings else None
        r_date = reference_readings[0].collection_date if reference_readings else None

        overall = (
            f"Compared with reference report, {improved} biomarker(s) improved, "
            f"{unchanged} remained unchanged, and {worsened} showed worsening."
        )

        return ComparisonResult(
            comparison_mode=mode,
            target_report_id=target_report_id,
            reference_report_id=reference_report_id,
            target_date=t_date,
            reference_date=r_date,
            health_score_delta=score_delta,
            improved_count=improved,
            unchanged_count=unchanged,
            worsened_count=worsened,
            biomarker_changes=changes,
            overall_clinical_assessment=overall,
        )


change_analyzer = ChangeAnalyzer()
