# --------------------------------------------------
# File: registry.py
# Purpose: Interaction Checker Registry.
# Module: Medicine Interaction Engine
# Used By: Medicine Services & API Controllers
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.interactions.checker import interaction_checker, InteractionChecker


class InteractionRegistry:
    def evaluate_safety(self, generic_names, is_pregnant=False):
        return interaction_checker.evaluate_safety(generic_names, is_pregnant=is_pregnant)


interaction_registry = InteractionRegistry()
