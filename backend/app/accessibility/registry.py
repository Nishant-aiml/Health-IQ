# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Accessibility Engine.
# Module: Accessibility Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from backend.app.accessibility.simplifier import medical_term_simplifier, MedicalTermSimplifier


class AccessibilityRegistry:
    def get_simplifier(self) -> MedicalTermSimplifier:
        return medical_term_simplifier


accessibility_registry = AccessibilityRegistry()
