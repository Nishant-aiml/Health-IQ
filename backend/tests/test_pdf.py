# --------------------------------------------------
# File: test_pdf.py
# Purpose: Unit tests for ReportLab PDF generator.
# Module: Backend Test Suite / PDF Engine
# Used By: Pytest Execution
# Future Phase: Phase 2E Validation
# --------------------------------------------------

from backend.app.pdf.generator import pdf_generator


def test_pdf_report_generation():
    analysis = {
        "report_id": 1,
        "source_filename": "patient_lab.pdf",
        "extraction_method_used": "PyMuPDFProvider",
        "health_score": 78,
        "summary": "Mild metabolic imbalance detected.",
        "parameters": [
            {
                "canonical_name": "Hemoglobin",
                "value": 11.5,
                "unit": "g/dL",
                "normal_range_low": 13.8,
                "normal_range_high": 17.2,
                "severity": "moderate",
                "is_critical": False,
            }
        ],
        "critical_alerts": [],
        "detected_patterns": [],
    }

    bundle = {
        "recommendations": [
            {
                "title": "Iron Intake Guidance",
                "priority": "HIGH",
                "summary": "Increase dietary iron.",
                "explanation": "Low hemoglobin levels benefit from iron-rich foods.",
                "category": "lifestyle",
            }
        ],
        "doctor_questions": [{"question_text": "Should I test ferritin levels?", "target_parameter": "Hemoglobin"}],
        "eli10_explanation": "Your blood needs more iron delivery trucks.",
        "limitations": [{"notice": "Educational report only."}],
    }

    pdf_bytes = pdf_generator.generate_report_pdf(analysis, bundle)

    assert len(pdf_bytes) > 0
    assert pdf_bytes.startswith(b"%PDF")
