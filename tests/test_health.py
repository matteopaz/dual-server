from fastapi.testclient import TestClient

def test_read_root(client: TestClient) -> None:
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
