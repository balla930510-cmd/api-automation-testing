import pytest


@pytest.mark.parametrize(
    "payload, expected_status, expected_error",
    [
        (
            {
                "barcode": "1234567890123",
                "amount": 100
            },
            200,
            None
        ),
        (
            {
                "barcode": "7777777777777",
                "amount": 0
            },
            400,
            "INVALID_AMOUNT"
        ),
        (
            {
                "barcode": "6666666666666",
                "amount": -100
            },
            400,
            "INVALID_AMOUNT"
        ),
        (
            {
                "barcode": "5555555555555",
                "amount": "abc"
            },
            400,
            "INVALID_AMOUNT"
        ),
        (
            {
                "barcode": "0000000000000",
                "amount": 100
            },
            400,
            "INVALID_BARCODE"
        ),
    ]
)
def test_payment(
    api_client,
    reset_test_data,
    payload,
    expected_status,
    expected_error
):

    response = api_client.post(
        "/api/payment",
        json=payload
    )

    assert response.status_code == expected_status

    data = response.json()

    if expected_status == 200:
        assert data["status"] == "SUCCESS"
        assert data["barcode"] == payload["barcode"]
        assert data["amount"] == payload["amount"]
        assert "transaction_id" in data

    else:
        assert data["status"] == "FAILED"
        assert data["error_code"] == expected_error


def test_payment_without_amount(api_client, reset_test_data):

    payload = {
        "barcode": "1234567890123"
    }

    response = api_client.post(
        "/api/payment",
        json=payload
    )

    assert response.status_code == 400

    data = response.json()

    assert data["status"] == "FAILED"
    assert data["error_code"] == "AMOUNT_REQUIRED"


def test_duplicate_payment(
    api_client,
    reset_test_data
):

    payload = {
        "barcode": "7777777777777",
        "amount": 200
    }

    first_response = api_client.post(
        "/api/payment",
        json=payload
    )

    assert first_response.status_code == 200
    assert first_response.json()["status"] == "SUCCESS"

    second_response = api_client.post(
        "/api/payment",
        json=payload
    )

    assert second_response.status_code == 400

    data = second_response.json()

    assert data["status"] == "FAILED"
    assert data["error_code"] == "BARCODE_ALREADY_USED"