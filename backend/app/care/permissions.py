# --------------------------------------------------
# File: permissions.py
# Purpose: Care Team permissions matrix enforcing viewer-only access control.
# Module: Care Team Engine / Permissions
# Used By: Clinical Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.care.models import CareTeamMember, CareTeamRole
from backend.app.care.roles import DEFAULT_ROLE_METADATA


class CareTeamPermissionValidator:
    """Validates care team viewer permissions."""

    def can_access_package(self, member: CareTeamMember, report_id: int) -> bool:
        if member.assigned_report_ids and report_id not in member.assigned_report_ids:
            return False
        return True

    def can_add_notes(self, member: CareTeamMember) -> bool:
        meta = DEFAULT_ROLE_METADATA.get(member.role, {})
        return meta.get("can_add_clinical_notes", False)


care_team_permission_validator = CareTeamPermissionValidator()
