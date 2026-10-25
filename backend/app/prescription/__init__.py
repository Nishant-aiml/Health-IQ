# --------------------------------------------------
# File: __init__.py
# Purpose: Prescription OCR & Parsing package index.
# Module: Prescription OCR & Parsing
# Used By: Prescription Services
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.prescription.models import RawPrescriptionItem, PrescriptionParseResult
from backend.app.prescription.normalizer import normalize_prescription_line, normalize_dosage_string
from backend.app.prescription.parser import PrescriptionParser, prescription_parser
from backend.app.prescription.extractor import PrescriptionExtractor, prescription_extractor
from backend.app.prescription.registry import PrescriptionRegistry, prescription_registry

__all__ = [
    "RawPrescriptionItem",
    "PrescriptionParseResult",
    "normalize_prescription_line",
    "normalize_dosage_string",
    "PrescriptionParser",
    "prescription_parser",
    "PrescriptionExtractor",
    "prescription_extractor",
    "PrescriptionRegistry",
    "prescription_registry",
]
