import pytest


@pytest.mark.parametrize(
    "barcode, expected_status, expected_error",
    [
        ("1234567890123", 200, None),
        ("0000000000000", 400, "INVALID_BARCODE"),
        ("9999999999999", 400, "BARCODE_EXPIRED"),
        ("8888888888888", 400, "BARCODE_ALREADY_USED"),
    ]
)
def test_scan_barcode(
    api_client,
    barcode,
    expected_status,
    expected_error
):

    payload = {
        "barcode": barcode
    }

    response = api_client.post(
        "/api/barcode/scan",
        json=payload
    )

    assert response.status_code == expected_status

    data = response.json()

    if expected_status == 200:
        assert data["status"] == "SUCCESS"
        assert data["barcode"] == barcode

    else:
        assert data["status"] == "FAILED"
        assert data["error_code"] == expected_error


def test_scan_without_barcode(api_client):

    response = api_client.post(
        "/api/barcode/scan",
        json={}
    )

    assert response.status_code == 400

    data = response.json()

    assert data["status"] == "FAILED"
    assert data["error_code"] == "BARCODE_REQUIRED"