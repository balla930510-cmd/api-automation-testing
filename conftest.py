import pytest

from api.api_client import APIClient
from config.config import (
    USER_API_BASE_URL,
    PAYMENT_API_BASE_URL
)


@pytest.fixture
def user_api_client():
    return APIClient(USER_API_BASE_URL)


@pytest.fixture
def api_client():
    return APIClient(PAYMENT_API_BASE_URL)


@pytest.fixture(autouse=True)
def reset_test_data(api_client):

    response = api_client.post("/api/test/reset")

    assert response.status_code == 200
    assert response.json()["status"] == "RESET_SUCCESS"