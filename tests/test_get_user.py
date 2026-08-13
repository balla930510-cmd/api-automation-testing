def test_get_user(user_api_client):

    response = user_api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1