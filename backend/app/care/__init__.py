# --------------------------------------------------
# File: __init__.py
# Purpose: Care Team Engine package index.
# Module: Care Team Engine
# Used By: Services & Application
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.care.models import CareTeamRole, CareTeamMember
from backend.app.care.roles import DEFAULT_ROLE_METADATA
from backend.app.care.permissions import CareTeamPermissionValidator, care_team_permission_validator
from backend.app.care.registry import CareTeamRegistry, care_team_registry

__all__ = [
    "CareTeamRole",
    "CareTeamMember",
    "DEFAULT_ROLE_METADATA",
    "CareTeamPermissionValidator",
    "care_team_permission_validator",
    "CareTeamRegistry",
    "care_team_registry",
]
