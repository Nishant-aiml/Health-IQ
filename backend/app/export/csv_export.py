# --------------------------------------------------
# File: csv_export.py
# Purpose: Multi-dataset CSV Report Export Generator (Parameters, Recommendations, Critical Alerts).
# Module: Export Engine
# Used By: Export APIs & Download Service
# Future Phase: Phase 2E Export System
# --------------------------------------------------

import csv
from io import StringIO
from typing import Dict, Any


class CSVExportService:
    """
    CSV Export Service.

    Why it exists:
        Generates CSV format exports of extracted laboratory parameters, recommendations, and critical alerts.
    """

    def generate_csv_export(
        self,
        analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
    ) -> str:
        output = StringIO()
        writer = csv.writer(output)

        # Section 1: Report Metadata
        writer.writerow(["=== HEALTHLENS AI REPORT SUMMARY ==="])
        writer.writerow(["Report ID", analysis.get("report_id")])
        writer.writerow(["Source File", analysis.get("source_filename")])
        writer.writerow(["Health Score", analysis.get("health_score")])
        writer.writerow(["OCR Method", analysis.get("extraction_method_used")])
        writer.writerow([])

        # Section 2: Extracted Parameters
        writer.writerow(["=== EXTRACTED LABORATORY PARAMETERS ==="])
        writer.writerow(["Parameter Name", "Value", "Unit", "Normal Low", "Normal High", "Severity", "Critical Alert"])
        for p in analysis.get("parameters", []):
            writer.writerow(
                [
                    p.get("canonical_name"),
                    p.get("value"),
                    p.get("unit"),
                    p.get("normal_range_low"),
                    p.get("normal_range_high"),
                    p.get("severity"),
                    "YES" if p.get("is_critical") else "NO",
                ]
            )
        writer.writerow([])

        # Section 3: Recommendations
        writer.writerow(["=== ACTION RECOMMENDATIONS ==="])
        writer.writerow(["Priority", "Title", "Summary", "Category"])
        for r in recommendation_bundle.get("recommendations", []):
            writer.writerow([r.get("priority"), r.get("title"), r.get("summary"), r.get("category")])

        return output.getvalue()


csv_export_service = CSVExportService()
