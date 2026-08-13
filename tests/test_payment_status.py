def test_get_payment_status(api_client):

    payment_payload = {
        "barcode": "1234567890123",
        "amount": 100
    }

    payment_response = api_client.post(
        "/api/payment",
        json=payment_payload
    )

    assert payment_response.status_code == 200

    payment_data = payment_response.json()

    transaction_id = payment_data["transaction_id"]

    response = api_client.get(
        f"/api/payment/{transaction_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "SUCCESS"
    assert data["transaction_id"] == transaction_id
    assert data["barcode"] == "1234567890123"
    assert data["amount"] == 100
    assert data["merchant"] == "Test Store"
    
def test_get_nonexistent_payment(api_client):

    response = api_client.get(
        "/api/payment/TX-99999"
    )

    assert response.status_code == 404

    data = response.json()

    assert data["status"] == "FAILED"
    assert data["error_code"] == "TRANSACTION_NOT_FOUND"