# --------------------------------------------------
# File: test_medicine_api.py
# Purpose: Integration tests for /api/v1/prescriptions API endpoints.
# Module: Backend Test Suite / Prescriptions API
# Used By: Pytest Execution
# Future Phase: Phase 3A Validation
# --------------------------------------------------

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_prescription_analyze_pasted_text():
    pasted_text = (
        "PRESCRIPTION\n"
        "Tab. Glycomet 500mg BD PC 7 days\n"
        "Tab. Atorvastatin 10mg HS\n"
    )

    response = client.post("/api/v1/prescriptions/analyze", data={"pasted_text": pasted_text})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert len(json_data["data"]["medicines"]) == 2
    assert "prescription_id" in json_data["data"]
