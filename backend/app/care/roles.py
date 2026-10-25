# --------------------------------------------------
# File: roles.py
# Purpose: Care team role definitions and default metadata.
# Module: Care Team Engine / Roles
# Used By: Permissions & Care Engine
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Dict, Any
from backend.app.care.models import CareTeamRole

DEFAULT_ROLE_METADATA: Dict[CareTeamRole, Dict[str, Any]] = {
    CareTeamRole.PRIMARY_DOCTOR: {
        "can_view_full_report": True,
        "can_add_clinical_notes": True,
        "can_view_evidence_graph": True,
        "package_access_level": "FULL_CLINICAL",
    },
    CareTeamRole.SPECIALIST: {
        "can_view_full_report": True,
        "can_add_clinical_notes": True,
        "can_view_evidence_graph": True,
        "package_access_level": "SPECIALTY_SPECIFIC",
    },
    CareTeamRole.DIETITIAN: {
        "can_view_full_report": True,
        "can_add_clinical_notes": True,
        "can_view_evidence_graph": True,
        "package_access_level": "NUTRITION_LIFESTYLE",
    },
    CareTeamRole.CAREGIVER: {
        "can_view_full_report": True,
        "can_add_clinical_notes": False,
        "can_view_evidence_graph": False,
        "package_access_level": "PATIENT_FRIENDLY",
    },
    CareTeamRole.FAMILY: {
        "can_view_full_report": False,
        "can_add_clinical_notes": False,
        "can_view_evidence_graph": False,
        "package_access_level": "FAMILY_SUMMARY",
    },
}
