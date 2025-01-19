def test_chatbot_endpoint(test_client):
    response = test_client.post("/chat/", json={"query": "What are your services?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] == "Processing query: What are your services?"
