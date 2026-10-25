# --------------------------------------------------
# File: summary.py
# Purpose: PDF Health Score gauge and penalty breakdown section component.
# Module: PDF Engine / Components
# Used By: PDF Section Builder
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from typing import Dict, Any, List
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from backend.app.pdf.styles import medical_pdf_styles


def build_health_score_section(analysis: Dict[str, Any]) -> List[Any]:
    elements = []

    elements.append(Paragraph("1. Overall Health Score & Clinical Summary", medical_pdf_styles.h2_style))

    score = analysis.get("health_score", 100)
    score_color = medical_pdf_styles.SUCCESS_GREEN
    if score < 60:
        score_color = medical_pdf_styles.CRITICAL_ROSE
    elif score < 80:
        score_color = medical_pdf_styles.WARNING_AMBER

    summary_text = analysis.get("summary", "Laboratory report parameters processed.")

    score_card_data = [
        [
            Paragraph(f"<font size=18 color='{score_color.hexval()}'><b>{score} / 100</b></font><br/><b>Overall Health Score</b>", medical_pdf_styles.table_body_style),
            Paragraph(f"<b>Summary:</b><br/>{summary_text}", medical_pdf_styles.table_body_style),
        ]
    ]

    score_table = Table(score_card_data, colWidths=[120, 360])
    score_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), medical_pdf_styles.LIGHT_BG),
                ("BOX", (0, 0), (-1, -1), 0.5, medical_pdf_styles.BORDER_COLOR),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(score_table)
    return elements
