# --------------------------------------------------
# File: __init__.py
# Purpose: PDF Components package index.
# Module: PDF Engine / Components
# Used By: PDF Section Builder
# Future Phase: Phase 2E
# --------------------------------------------------

from backend.app.pdf.components.cover import build_cover_header
from backend.app.pdf.components.summary import build_health_score_section
from backend.app.pdf.components.tables import build_parameters_table
from backend.app.pdf.components.recommendations import build_recommendations_section
from backend.app.pdf.components.footer import NumberedCanvas

__all__ = [
    "build_cover_header",
    "build_health_score_section",
    "build_parameters_table",
    "build_recommendations_section",
    "NumberedCanvas",
]
