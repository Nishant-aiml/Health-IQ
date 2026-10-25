# --------------------------------------------------
# File: test_prescription_parser.py
# Purpose: Unit tests for prescription parser and OCR line normalizer.
# Module: Backend Test Suite / Prescription Engine
# Used By: Pytest Execution
# Future Phase: Phase 3A Validation
# --------------------------------------------------

from backend.app.prescription.parser import prescription_parser


def test_prescription_parsing_standard():
    ocr_text = (
        "PRESCRIPTION\n"
        "Tab. Glycomet 500mg BD PC 7 days\n"
        "Cap. Augmentin 625mg TDS PC 5 days\n"
        "Tab. Atorvastatin 10mg HS\n"
        "Tab. Dolo 650mg SOS\n"
    )

    items = prescription_parser.parse_text(ocr_text)

    assert len(items) == 4
    med_names = [item.medicine_name_raw for item in items]
    assert any("Glycomet" in m for m in med_names)
    assert any("Augmentin" in m for m in med_names)
    assert any("Atorvastatin" in m for m in med_names)
    assert any("Dolo" in m for m in med_names)
