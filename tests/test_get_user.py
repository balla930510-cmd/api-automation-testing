from api.api_client import APIClient

client = APIClient()


def test_get_user():

    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1