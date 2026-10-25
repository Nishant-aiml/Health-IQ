from fastapi.testclient import TestClient


def test_404_not_found_handling(client: TestClient):
    response = client.get("/api/v1/non_existent_endpoint")
    assert response.status_code == 404
