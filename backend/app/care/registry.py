# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Care Team Engine.
# Module: Care Team Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.care.permissions import care_team_permission_validator, CareTeamPermissionValidator


class CareTeamRegistry:
    def get_validator(self) -> CareTeamPermissionValidator:
        return care_team_permission_validator


care_team_registry = CareTeamRegistry()
