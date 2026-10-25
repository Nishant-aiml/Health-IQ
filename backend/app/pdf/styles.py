# --------------------------------------------------
# File: styles.py
# Purpose: Professional ReportLab stylesheet tokens and color palettes.
# Module: PDF Engine
# Used By: PDF Components & Renderer
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


class MedicalPDFStyles:
    """
    ReportLab Medical PDF Stylesheet.

    Why it exists:
        Provides clean, modern, hospital-quality typography, margins, and hex color palettes.
    """

    # Color Palette
    PRIMARY_TEAL = colors.HexColor("#0d9488")
    SECONDARY_INDIGO = colors.HexColor("#4f46e5")
    DARK_SLATE = colors.HexColor("#0f172a")
    MUTED_SLATE = colors.HexColor("#64748b")
    LIGHT_BG = colors.HexColor("#f8fafc")
    BORDER_COLOR = colors.HexColor("#e2e8f0")
    CRITICAL_ROSE = colors.HexColor("#e11d48")
    WARNING_AMBER = colors.HexColor("#d97706")
    SUCCESS_GREEN = colors.HexColor("#059669")

    def __init__(self):
        self.base_styles = getSampleStyleSheet()

        self.title_style = ParagraphStyle(
            "MedicalTitle",
            parent=self.base_styles["Heading1"],
            fontSize=22,
            leading=26,
            textColor=self.PRIMARY_TEAL,
            fontName="Helvetica-Bold",
            spaceAfter=6,
        )

        self.subtitle_style = ParagraphStyle(
            "MedicalSubtitle",
            parent=self.base_styles["Normal"],
            fontSize=10,
            leading=13,
            textColor=self.MUTED_SLATE,
            fontName="Helvetica",
            spaceAfter=14,
        )

        self.h2_style = ParagraphStyle(
            "MedicalH2",
            parent=self.base_styles["Heading2"],
            fontSize=14,
            leading=18,
            textColor=self.DARK_SLATE,
            fontName="Helvetica-Bold",
            spaceBefore=12,
            spaceAfter=8,
        )

        self.body_style = ParagraphStyle(
            "MedicalBody",
            parent=self.base_styles["Normal"],
            fontSize=9.5,
            leading=13.5,
            textColor=self.DARK_SLATE,
            fontName="Helvetica",
            spaceAfter=6,
        )

        self.table_header_style = ParagraphStyle(
            "TableHeader",
            parent=self.base_styles["Normal"],
            fontSize=9,
            leading=11,
            textColor=colors.white,
            fontName="Helvetica-Bold",
        )

        self.table_body_style = ParagraphStyle(
            "TableBody",
            parent=self.base_styles["Normal"],
            fontSize=8.5,
            leading=11,
            textColor=self.DARK_SLATE,
            fontName="Helvetica",
        )


medical_pdf_styles = MedicalPDFStyles()
