from fastapi.testclient import TestClient


def test_version_endpoint(client: TestClient):
    response = client.get("/api/v1/version")
    assert response.status_code == 200

    payload = response.json()
    assert payload["success"] is True
    assert payload["data"]["name"] == "AI Health Intelligence Platform"
    assert payload["data"]["version"] == "0.1.0"
    assert payload["data"]["api_version"] == "/api/v1"
