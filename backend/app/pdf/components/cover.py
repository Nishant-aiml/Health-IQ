# --------------------------------------------------
# File: cover.py
# Purpose: PDF cover header and patient overview component.
# Module: PDF Engine / Components
# Used By: PDF Section Builder
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from typing import Dict, Any, List
from reportlab.platypus import Paragraph, HRFlowable, Table, TableStyle
from reportlab.lib import colors
from backend.app.pdf.styles import medical_pdf_styles


def build_cover_header(analysis: Dict[str, Any]) -> List[Any]:
    elements = []

    # Title & Subtitle
    elements.append(Paragraph("HealthLens AI — Laboratory Health Intelligence", medical_pdf_styles.title_style))
    elements.append(
        Paragraph(
            f"Official Diagnostic Intelligence Summary • Source File: {analysis.get('source_filename')} • Processed via {analysis.get('extraction_method_used')}",
            medical_pdf_styles.subtitle_style,
        )
    )

    # Accent Line
    elements.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=medical_pdf_styles.PRIMARY_TEAL,
            spaceAfter=14,
        )
    )

    # Patient Metadata Overview Box
    meta_data = [
        [
            Paragraph("<b>Report ID:</b> #" + str(analysis.get("report_id")), medical_pdf_styles.table_body_style),
            Paragraph("<b>Extraction Method:</b> " + str(analysis.get("extraction_method_used")), medical_pdf_styles.table_body_style),
        ],
        [
            Paragraph("<b>Extracted Parameters:</b> " + str(len(analysis.get("parameters", []))), medical_pdf_styles.table_body_style),
            Paragraph("<b>Critical Alerts:</b> " + str(len(analysis.get("critical_alerts", []))), medical_pdf_styles.table_body_style),
        ],
    ]
    meta_table = Table(meta_data, colWidths=[240, 240])
    meta_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), medical_pdf_styles.LIGHT_BG),
                ("BOX", (0, 0), (-1, -1), 0.5, medical_pdf_styles.BORDER_COLOR),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    elements.append(meta_table)
    return elements
