def test_update_user(user_api_client):

    payload = {
        "name": "Updated User",
        "job": "Senior QA"
    }

    response = user_api_client.put(
        "/users/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["job"] == payload["job"]