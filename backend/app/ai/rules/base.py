# --------------------------------------------------
# File: base.py
# Purpose: Abstract base class for clinical recommendation rule engines.
# Module: AI Engine / Rules
# Used By: Recommendation Rules & Recommendation Registry
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from backend.app.ai.models import Recommendation


class ClinicalRule(ABC):
    """
    Abstract Base Class for Clinical Recommendation Rules.

    Why it exists:
        Enforces a common interface (`evaluate`) for all clinical recommendation engines
        (anemia, metabolic, renal, thyroid, liver), allowing the registry to execute
        them generically.
    """

    def __init__(self, rule_name: str):
        self.rule_name = rule_name

    @abstractmethod
    def evaluate(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
    ) -> List[Recommendation]:
        """
        Evaluates extracted lab parameters and detected patterns, returning structured Recommendation objects.
        """
        pass
