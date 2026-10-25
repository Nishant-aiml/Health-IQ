from fastapi.testclient import TestClient


def test_health_check_endpoint(client: TestClient):
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    payload = response.json()
    assert payload["success"] is True
    assert "data" in payload
    assert payload["data"]["status"] == "healthy"
    assert payload["data"]["database"] == "connected"
    assert "X-Process-Time" in response.headers
    assert "X-Request-ID" in response.headers
