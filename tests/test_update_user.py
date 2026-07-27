from api.api_client import APIClient
from data.test_data import UPDATE_USER

client = APIClient()


def test_update_user():

    response = client.put(
        "/users/1",
        UPDATE_USER
    )

    assert response.status_code == 200

    data = response.json()

    assert data["job"] == UPDATE_USER["job"]