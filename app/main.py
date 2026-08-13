from flask import Flask, jsonify, request

app = Flask(__name__)


# Mock barcode database
import copy
INITIAL_BARCODES = {
    "1234567890123": {
        "status": "VALID",
        "merchant": "Test Store",
        "amount": 100
    },

    "7777777777777": {
        "status": "VALID",
        "merchant": "Test Store",
        "amount": 200
    },

    "6666666666666": {
        "status": "VALID",
        "merchant": "Test Store",
        "amount": 300
    },

    "5555555555555": {
        "status": "VALID",
        "merchant": "Test Store",
        "amount": 400
    },

    "4444444444444": {
        "status": "VALID",
        "merchant": "Test Store",
        "amount": 500
    },

    "9999999999999": {
        "status": "EXPIRED",
        "merchant": "Test Store",
        "amount": 100
    },

    "8888888888888": {
        "status": "USED",
        "merchant": "Test Store",
        "amount": 100
    }
}

BARCODES = copy.deepcopy(INITIAL_BARCODES)

TRANSACTIONS = {}

@app.post("/api/barcode/scan")
def scan_barcode():
    data = request.get_json()

    if not data or "barcode" not in data:
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_REQUIRED"
        }), 400

    barcode = data["barcode"]

    if barcode not in BARCODES:
        return jsonify({
            "status": "FAILED",
            "error_code": "INVALID_BARCODE"
        }), 400

    barcode_info = BARCODES[barcode]

    if barcode_info["status"] == "EXPIRED":
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_EXPIRED"
        }), 400

    if barcode_info["status"] == "USED":
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_ALREADY_USED"
        }), 400

    return jsonify({
        "status": "SUCCESS",
        "barcode": barcode,
        "merchant": barcode_info["merchant"],
        "amount": barcode_info["amount"]
    }), 200

@app.post("/api/payment")
def make_payment():
    data = request.get_json()

    # Check required fields
    if not data:
        return jsonify({
            "status": "FAILED",
            "error_code": "REQUEST_REQUIRED"
        }), 400

    if "barcode" not in data:
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_REQUIRED"
        }), 400

    if "amount" not in data:
        return jsonify({
            "status": "FAILED",
            "error_code": "AMOUNT_REQUIRED"
        }), 400

    barcode = data["barcode"]
    amount = data["amount"]

    # Validate barcode
    if barcode not in BARCODES:
        return jsonify({
            "status": "FAILED",
            "error_code": "INVALID_BARCODE"
        }), 400

    barcode_info = BARCODES[barcode]

    if barcode_info["status"] == "EXPIRED":
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_EXPIRED"
        }), 400

    if barcode_info["status"] == "USED":
        return jsonify({
            "status": "FAILED",
            "error_code": "BARCODE_ALREADY_USED"
        }), 400

    # Validate amount
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return jsonify({
            "status": "FAILED",
            "error_code": "INVALID_AMOUNT"
        }), 400

    if amount <= 0:
        return jsonify({
            "status": "FAILED",
            "error_code": "INVALID_AMOUNT"
        }), 400

    transaction_id = f"TX-{len(TRANSACTIONS) + 10001}"
    TRANSACTIONS[transaction_id] = {
        "status": "SUCCESS",
        "transaction_id": transaction_id,
        "barcode": barcode,
        "amount": amount,
        "merchant": barcode_info["merchant"]
    }
    barcode_info["status"] = "USED"

    return jsonify(
        TRANSACTIONS[transaction_id]
        ), 200

@app.get("/api/payment/<transaction_id>")
def get_payment(transaction_id):

    if transaction_id not in TRANSACTIONS:
        return jsonify({
            "status": "FAILED",
            "error_code": "TRANSACTION_NOT_FOUND"
        }), 404

    return jsonify(
        TRANSACTIONS[transaction_id]
    ), 200

@app.post("/api/test/reset")
def reset_test_data():

    global BARCODES
    global TRANSACTIONS

    BARCODES = copy.deepcopy(INITIAL_BARCODES)
    TRANSACTIONS = {}

    return jsonify({
        "status": "RESET_SUCCESS"
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)