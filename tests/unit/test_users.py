def test_get_users(test_client):
    response = test_client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json()["users"], list)
