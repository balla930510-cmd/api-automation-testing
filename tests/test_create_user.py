def test_create_user(user_api_client):

    payload = {
        "name": "Test User",
        "job": "QA"
    }

    response = user_api_client.post(
        "/users",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
