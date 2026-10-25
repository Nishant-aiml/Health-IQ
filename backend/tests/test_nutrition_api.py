# --------------------------------------------------
# File: test_nutrition_api.py
# Purpose: Integration tests for /api/v1/nutrition, /api/v1/lifestyle, and /api/v1/wellness endpoints.
# Module: Backend Test Suite / Nutrition API
# Used By: Pytest Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_get_nutrition_api():
    response = client.get("/api/v1/nutrition/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "recommendations" in json_data["data"]
    assert "food_interactions" in json_data["data"]


def test_get_lifestyle_api():
    response = client.get("/api/v1/lifestyle/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "exercise_plan" in json_data["data"]
    assert "sleep_hygiene" in json_data["data"]


def test_get_wellness_api():
    response = client.get("/api/v1/wellness/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "overall_wellness_score" in json_data["data"]
