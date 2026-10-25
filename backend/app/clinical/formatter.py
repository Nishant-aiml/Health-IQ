# --------------------------------------------------
# File: formatter.py
# Purpose: Formats Clinical Case Packages for Doctor, Patient, and Family audiences.
# Module: Clinical Collaboration Engine / Formatter
# Used By: Clinical Service & Export
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Dict, Any
from backend.app.clinical.models import ClinicalCasePackage, AudienceTarget


class ClinicalPackageFormatter:
    """Formats Clinical Case Packages according to the recipient audience perspective."""

    def format_package_for_audience(self, package: ClinicalCasePackage, audience: AudienceTarget) -> Dict[str, Any]:
        data = package.model_dump()
        data["audience"] = audience.value

        if audience == AudienceTarget.DOCTOR:
            data["active_summary"] = package.doctor_summary
            data["header_title"] = "Physician Clinical Case Brief"
        elif audience == AudienceTarget.PATIENT:
            data["active_summary"] = package.patient_summary
            data["header_title"] = "Personal Health Report Summary"
        elif audience == AudienceTarget.FAMILY:
            data["active_summary"] = f"Family Care Summary: {package.patient_summary}"
            data["header_title"] = "Family Caregiver Overview"

        return data


clinical_package_formatter = ClinicalPackageFormatter()
