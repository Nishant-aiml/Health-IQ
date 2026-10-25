# --------------------------------------------------
# File: test_evidence_builder.py
# Purpose: Unit tests for evidence chain builder.
# Module: Backend Test Suite / AI Engine
# Used By: Pytest Execution
# Future Phase: Phase 2C Validation
# --------------------------------------------------

from backend.app.ai.recommendation import recommendation_engine
from backend.app.ai.evidence import evidence_builder


def test_evidence_chain_generation():
    params = {
        "Hemoglobin": {"value": 11.0, "unit": "g/dL", "severity": "moderate", "normal_range_low": 13.8, "normal_range_high": 17.2},
    }
    recs = recommendation_engine.generate_recommendations(params, [])
    chains = evidence_builder.build_evidence_chains(params, [], recs)

    assert len(chains) >= 1
    assert chains[0].parameter_name == "Hemoglobin"
    assert chains[0].observed_value == 11.0
    assert len(chains[0].reasoning_chain) >= 4
