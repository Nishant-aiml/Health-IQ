# --------------------------------------------------
# File: registry.py
# Purpose: Pattern Registry orchestrator executing cross-parameter clinical rules.
# Module: Analysis Engine / Patterns
# Used By: Worker Queue Jobs & Report Service
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.analysis.patterns.base import PatternRule
from backend.app.analysis.patterns.anemia import AnemiaPatternRule
from backend.app.analysis.patterns.metabolic import MetabolicPatternRule
from backend.app.analysis.patterns.renal import RenalPatternRule
from backend.app.analysis.patterns.thrombocyte import ThrombocytePatternRule
from backend.app.core.logging import logger


class PatternRegistry:
    """
    Pattern Registry Orchestrator.

    Why it exists:
        Maintains an active registry of `PatternRule` instances. Iterates over extracted lab parameters,
        evaluates each rule, and returns a clean list of structured detected pattern objects.
    """

    def __init__(self, rules: List[PatternRule] = None):
        self.rules = rules or [
            AnemiaPatternRule(),
            MetabolicPatternRule(),
            RenalPatternRule(),
            ThrombocytePatternRule(),
        ]

    def evaluate_all(self, extracted_parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Evaluates all active clinical pattern rules against extracted parameters.

        Inputs:
            extracted_parameters: Dict mapping parameter names to value objects.

        Returns:
            List of structured detected pattern dicts.
        """
        detected_patterns: List[Dict[str, Any]] = []

        for rule in self.rules:
            try:
                result = rule.evaluate(extracted_parameters)
                if result:
                    detected_patterns.append(result)
            except Exception as exc:
                logger.error(f"Error evaluating pattern rule '{rule.pattern_name}': {exc}")

        return detected_patterns


pattern_registry = PatternRegistry()
