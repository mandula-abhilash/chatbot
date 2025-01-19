def test_health_check(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}

def test_invalid_chat_request(test_client):
    response = test_client.post("/chat/", json={})
    assert response.status_code == 422  # Unprocessable entity due to missing query
