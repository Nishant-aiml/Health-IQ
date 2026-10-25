# --------------------------------------------------
# File: test_exports.py
# Purpose: Unit tests for Clinical Export Service and Care Team Viewer permissions.
# Module: Backend Test Suite / Clinical Export
# Used By: Pytest Execution
# Future Phase: Phase 4 Validation
# --------------------------------------------------

from backend.app.care.permissions import care_team_permission_validator
from backend.app.care.models import CareTeamMember, CareTeamRole


def test_care_team_permissions():
    doctor = CareTeamMember(member_id="m1", name="Dr. A", role=CareTeamRole.PRIMARY_DOCTOR, assigned_report_ids=[1, 2])
    family = CareTeamMember(member_id="m2", name="Family B", role=CareTeamRole.FAMILY, assigned_report_ids=[1])

    assert care_team_permission_validator.can_access_package(doctor, 1) is True
    assert care_team_permission_validator.can_access_package(doctor, 99) is False
    assert care_team_permission_validator.can_add_notes(doctor) is True
    assert care_team_permission_validator.can_add_notes(family) is False
