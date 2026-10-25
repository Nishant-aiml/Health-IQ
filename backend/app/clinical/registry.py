# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Clinical Case Package Generator.
# Module: Clinical Collaboration Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.clinical.builder import clinical_package_builder, ClinicalPackageBuilder
from backend.app.clinical.formatter import clinical_package_formatter, ClinicalPackageFormatter


class ClinicalRegistry:
    def get_builder(self) -> ClinicalPackageBuilder:
        return clinical_package_builder

    def get_formatter(self) -> ClinicalPackageFormatter:
        return clinical_package_formatter


clinical_registry = ClinicalRegistry()
