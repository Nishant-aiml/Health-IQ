# --------------------------------------------------
# File: base.py
# Purpose: Abstract base class for cross-parameter clinical pattern rules.
# Module: Analysis Engine / Patterns
# Used By: Pattern Rules & Pattern Registry
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any


class PatternRule(ABC):
    """
    Abstract Base Class for Cross-Parameter Pattern Detection Rules.

    Why it exists:
        Medical analysis reasons over combinations of abnormal lab values rather than
        each value independently (e.g. Low Hemoglobin + Low MCV = Microcytic Anemia).
        This base class decouples individual clinical rules so new pattern rules can be added cleanly.
    """

    def __init__(self, pattern_name: str):
        self.pattern_name = pattern_name

    @abstractmethod
    def evaluate(self, extracted_parameters: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Evaluates a set of extracted lab parameters for clinical pattern matching.

        Inputs:
            extracted_parameters: Dict mapping `canonical_name` -> `{value, unit, severity, normal_range_low, normal_range_high}`.

        Returns:
            Structured dict containing `pattern_name`, `confidence`, `triggered_by`, and `summary` if matched, else None.
        """
        pass
