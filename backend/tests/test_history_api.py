# --------------------------------------------------
# File: test_history_api.py
# Purpose: Integration tests for /api/v1/history API endpoints.
# Module: Backend Test Suite / History API
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_get_patient_history_api():
    response = client.get("/api/v1/history/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "user_id" in json_data["data"]


def test_get_patient_timeline_api():
    response = client.get("/api/v1/history/1/timeline")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "events" in json_data["data"]


def test_get_patient_trends_api():
    response = client.get("/api/v1/history/1/trends")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "biomarker_trends" in json_data["data"]
