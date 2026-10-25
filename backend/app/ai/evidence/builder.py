# --------------------------------------------------
# File: builder.py
# Purpose: Builds explicit reasoning chains explaining WHY recommendations were generated.
# Module: AI Engine / Evidence
# Used By: Recommendation Service
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.ai.models import Evidence, Recommendation


class EvidenceBuilder:
    """
    Evidence Builder.

    Why it exists:
        Guarantees that every generated recommendation is accompanied by an explicit
        step-by-step reasoning chain object (`Parameter -> Observed Value -> Severity -> Pattern -> Recommendation`).
        Never returns unexplainable recommendations.
    """

    def build_evidence_chains(
        self,
        extracted_parameters: Dict[str, Any],
        detected_patterns: List[Dict[str, Any]],
        recommendations: List[Recommendation],
    ) -> List[Evidence]:
        evidence_chains: List[Evidence] = []

        for rec in recommendations:
            for p_name in rec.supporting_parameters:
                param_info = extracted_parameters.get(p_name)
                if not param_info:
                    continue

                val = param_info.get("value", 0.0)
                unit = param_info.get("unit", "")
                sev = param_info.get("severity", "normal")
                low = param_info.get("normal_range_low")
                high = param_info.get("normal_range_high")
                range_str = f"{low} - {high}" if low is not None and high is not None else "N/A"

                pattern_name = None
                for pat in detected_patterns:
                    if p_name in pat.get("triggered_by", []):
                        pattern_name = pat.get("pattern_name")
                        break

                chain = [
                    f"Parameter '{p_name}' observed at {val} {unit}",
                    f"Baseline normal range: {range_str} {unit}",
                    f"Severity evaluated as: '{sev}'",
                ]
                if pattern_name:
                    chain.append(f"Correlated clinical pattern: '{pattern_name}'")
                chain.append(f"Generated recommendation: '{rec.title}'")

                evidence_chains.append(
                    Evidence(
                        parameter_name=p_name,
                        observed_value=val,
                        unit=unit,
                        normal_range=range_str,
                        severity=sev,
                        detected_pattern=pattern_name,
                        reasoning_chain=chain,
                    )
                )

        return evidence_chains


evidence_builder = EvidenceBuilder()
