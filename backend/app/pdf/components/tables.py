# --------------------------------------------------
# File: tables.py
# Purpose: PDF Extracted Lab Parameters table component with severity badges.
# Module: PDF Engine / Components
# Used By: PDF Section Builder
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from typing import Dict, Any, List
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from backend.app.pdf.styles import medical_pdf_styles


def build_parameters_table(analysis: Dict[str, Any]) -> List[Any]:
    elements = []

    elements.append(Paragraph("2. Extracted Laboratory Parameters", medical_pdf_styles.h2_style))

    table_data = [
        [
            Paragraph("Parameter Name", medical_pdf_styles.table_header_style),
            Paragraph("Observed Value", medical_pdf_styles.table_header_style),
            Paragraph("Reference Interval", medical_pdf_styles.table_header_style),
            Paragraph("Severity Status", medical_pdf_styles.table_header_style),
        ]
    ]

    for p in analysis.get("parameters", []):
        p_name = p.get("canonical_name", "Unknown")
        val = f"{p.get('value')} {p.get('unit', '')}"
        ref_low = p.get("normal_range_low")
        ref_high = p.get("normal_range_high")
        unit = p.get("unit", "")
        ref_str = f"{ref_low} - {ref_high} {unit}" if ref_low is not None else "N/A"
        sev = str(p.get("severity", "normal")).upper()

        table_data.append(
            [
                Paragraph(f"<b>{p_name}</b>", medical_pdf_styles.table_body_style),
                Paragraph(val, medical_pdf_styles.table_body_style),
                Paragraph(ref_str, medical_pdf_styles.table_body_style),
                Paragraph(f"<b>{sev}</b>", medical_pdf_styles.table_body_style),
            ]
        )

    param_table = Table(table_data, colWidths=[150, 110, 130, 90])
    param_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), medical_pdf_styles.PRIMARY_TEAL),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.5, medical_pdf_styles.BORDER_COLOR),
                ("PADDING", (0, 0), (-1, -1), 5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, medical_pdf_styles.LIGHT_BG]),
            ]
        )
    )

    elements.append(param_table)
    return elements
