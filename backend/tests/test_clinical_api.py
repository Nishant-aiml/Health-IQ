# --------------------------------------------------
# File: test_clinical_api.py
# Purpose: Integration tests for /api/v1/clinical and /api/v1/notes REST endpoints.
# Module: Backend Test Suite / Clinical API
# Used By: Pytest Execution
# Future Phase: Phase 4 Validation
# --------------------------------------------------

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_get_clinical_package_api():
    response = client.get("/api/v1/clinical/package?report_id=1&audience=Doctor-Friendly")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "sha256_integrity_hash" in json_data["data"]
    assert len(json_data["data"]["sha256_integrity_hash"]) == 64


def test_get_clinical_timeline_api():
    response = client.get("/api/v1/clinical/timeline?report_id=1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert "history" in json_data["data"]


def test_export_fhir_api():
    response = client.get("/api/v1/clinical/export?report_id=1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["success"] is True
    assert json_data["data"]["resourceType"] == "Bundle"


def test_clinical_notes_api():
    post_res = client.post(
        "/api/v1/notes",
        json={
            "report_id": 1,
            "user_id": 1,
            "author_name": "Dr. Test",
            "author_role": "Specialist Physician",
            "note_type": "Doctor Comment",
            "content": "Follow up fasting blood glucose in 4 weeks.",
        },
    )
    assert post_res.status_code == 200
    assert post_res.json()["success"] is True

    get_res = client.get("/api/v1/notes?report_id=1")
    assert get_res.status_code == 200
    assert len(get_res.json()["data"]) >= 1
