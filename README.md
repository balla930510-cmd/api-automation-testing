# API Automation Testing

使用 **Python、Requests** 與 **Pytest** 建立的 API 自動化測試專案。

本專案示範 REST API 自動化測試流程，包含 GET、POST、PUT、DELETE 四種 HTTP 方法，並採用企業常見的專案架構，將 API 操作、測試資料與設定分離，提高程式的可維護性。

---

## Features

* GET API Testing
* POST API Testing
* PUT API Testing
* DELETE API Testing
* Pytest Assertions
* Pytest Fixture (`conftest.py`)
* API Client 封裝
* Config 管理
* Test Data 分離
* HTML Test Report

---

## Project Structure

```text
api-automation-testing/
│
├── api/
│   └── api_client.py
│
├── config/
│   └── config.py
│
├── data/
│   └── test_data.py
│
├── tests/
│   ├── test_get_user.py
│   ├── test_create_user.py
│   ├── test_update_user.py
│   ├── test_delete_user.py
│   └── test_parameter.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Technologies

- Python
- Requests
- Pytest
- REST API
- JSON
- HTTP Methods (GET / POST / PUT / DELETE)
- Assertion Testing

---

## Test Cases

| Test Case   | Description             | Expected Result                                    |
| ----------- | ----------------------- | -------------------------------------------------- |
| GET User    | Get user information    | Status Code = 200                                  |
| POST User   | Create a new user       | Status Code = 201                                  |
| PUT User    | Update user information | Status Code = 200                                  |
| DELETE User | Delete a user           | Status Code = 200 *(JSONPlaceholder API behavior)* |

---

## Installation

Clone this repository:

```bash
git clone https://github.com/<your-username>/api-automation-testing.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Tests

Run all tests:

```bash
pytest
```

## HTML Test Report

Generate HTML report:

```bash
pytest --html=reports/report.html
---

## Test Environment

* Python 3.13
* Requests
* Pytest
* Windows 11

---

## Future Improvements

- API Authentication (Bearer Token)
- Response Schema Validation
- Logging
- Allure Report
- GitHub Actions (CI/CD)
- Docker

---

## Author

白晨亮
