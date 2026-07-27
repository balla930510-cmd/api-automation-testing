from api.api_client import APIClient

client = APIClient()


def test_create_user():

    payload = {

        "name": "Alice",

        "job": "QA Engineer"

    }

    response = client.post(
        "/users",
        payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
