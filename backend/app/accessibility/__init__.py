# --------------------------------------------------
# File: __init__.py
# Purpose: Accessibility Engine package index.
# Module: Accessibility Engine
# Used By: Services & Application
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from backend.app.accessibility.models import AccessibilityProfileType, AccessibilitySettings
from backend.app.accessibility.simplifier import MedicalTermSimplifier, medical_term_simplifier
from backend.app.accessibility.registry import AccessibilityRegistry, accessibility_registry

__all__ = [
    "AccessibilityProfileType",
    "AccessibilitySettings",
    "MedicalTermSimplifier",
    "medical_term_simplifier",
    "AccessibilityRegistry",
    "accessibility_registry",
]
