# --------------------------------------------------
# File: registry.py
# Purpose: Clinical Change Engine registry.
# Module: Clinical Change Engine
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.change.analyzer import change_analyzer, ChangeAnalyzer


class ChangeRegistry:
    def compare_reports(self, mode, target_id, ref_id, target_readings, ref_readings, target_score=100.0, ref_score=100.0):
        return change_analyzer.compare_reports(mode, target_id, ref_id, target_readings, ref_readings, target_score, ref_score)


change_registry = ChangeRegistry()
