# --------------------------------------------------
# File: recommendations.py
# Purpose: PDF Recommendations, Evidence Chains, Doctor Questions, ELI10, and Limitations component.
# Module: PDF Engine / Components
# Used By: PDF Section Builder
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from typing import Dict, Any, List
from reportlab.platypus import Paragraph
from backend.app.pdf.styles import medical_pdf_styles


def build_recommendations_section(recommendation_bundle: Dict[str, Any]) -> List[Any]:
    elements = []

    # 1. Action Recommendations
    elements.append(Paragraph("3. Clinical Action Recommendations", medical_pdf_styles.h2_style))
    recs = recommendation_bundle.get("recommendations", [])
    if not recs:
        elements.append(Paragraph("No abnormal action recommendations generated. All parameters within target baseline.", medical_pdf_styles.body_style))
    else:
        for r in recs:
            prio = r.get("priority", "INFORMATIONAL")
            title = r.get("title", "")
            summary = r.get("summary", "")
            expl = r.get("explanation", "")
            elements.append(Paragraph(f"• <b>[{prio}] {title}:</b> {summary}<br/><i>{expl}</i>", medical_pdf_styles.body_style))

    # 2. Doctor Consultation Discussion Questions
    questions = recommendation_bundle.get("doctor_questions", [])
    if questions:
        elements.append(Paragraph("4. Doctor Consultation Discussion Checklist", medical_pdf_styles.h2_style))
        for q in questions:
            elements.append(Paragraph(f"• <b>Ask Doctor:</b> \"{q.get('question_text')}\" (Target: {q.get('target_parameter')})", medical_pdf_styles.body_style))

    # 3. Simple Explanation (ELI10)
    eli10 = recommendation_bundle.get("eli10_explanation")
    if eli10:
        elements.append(Paragraph("5. Simple Non-Technical Explanation (ELI10)", medical_pdf_styles.h2_style))
        elements.append(Paragraph(f"<i>\"{eli10}\"</i>", medical_pdf_styles.body_style))

    # 4. Mandatory Limitations
    limitations = recommendation_bundle.get("limitations", [])
    if limitations:
        elements.append(Paragraph("6. Mandatory Clinical Limitations & Context", medical_pdf_styles.h2_style))
        for lim in limitations:
            elements.append(Paragraph(f"• {lim.get('notice')}", medical_pdf_styles.body_style))

    return elements
