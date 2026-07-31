# API Automation & Performance Testing

This project demonstrates REST API automation testing and performance testing using Python. It covers functional validation with Pytest and load testing with Locust, showcasing a complete API testing workflow.

## Features

✔ REST API Automation

✔ CRUD API Testing

✔ Modular API Client

✔ Test Data Management

✔ HTML Report Generation

✔ Performance Testing with Locust

✔ GitHub Ready

## 🛠 Technologies
| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Testing | Requests |
| Performance | Locust |
| Reporting | Pytest-html |
| Version Control | Git,GitHub |

## 📂 Project Structure

```text
API_Testing/
│
├── api/
├── config/
├── data/
├── tests/
├── reports/
├── locust-performance-testing/
│   ├── locustfile.py
│   ├── requirements.txt
│   └── README.md
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🏗 Architecture
```text
Pytest Test Cases
      │
      ▼
API Client (Requests)
      │
      ▼
ReqRes REST API
      │
      ▼
Response Validation
      │
      ▼
Assertion
      │
      ▼
HTML Report
      │
      ▼
Performance Report (Locust)
```

---

## 🔧 Installation

```bash
git clone https://github.com/balla930510-cmd/api-automation-testing.git

cd API_Testing

pip install -r requirements.txt
```
## 🚀 API Automation Testing

### Test Coverage

- GET
- POST
- PUT
- DELETE

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/users?page=2 | Retrieve user list |
| POST | /api/users | Create a new user |
| PUT | /api/users/2 | Update user |
| DELETE | /api/users/2 | Delete user |


### Framework

- Requests
- Pytest
- Pytest Fixture
- HTML Report

### Run Tests

```bash
pytest
pytest --html=reports/report.html

```
## ✅ Test Result Summary

| Item | Result |
|------|--------|
| Total Tests | 7 |
| Passed | 7 |
| Failed | 0 |
| Success Rate | 100% |
| Execution Time | 5 sec |

## 📄 HTML Test Report

The automated API test results are generated using **pytest-html**.

### Summary

- Total Tests: 7
- Passed: 7
- Failed: 0
- Errors: 0

### Report Screenshot

![Pytest HTML Report](reports/screenshot/pytest_html_report.png)


## ⚡ Performance Testing (Locust)

### Target API

```
https://reqres.in
```

### Test Scenario

- GET /api/users?page=2
- POST /api/users

### Run Locust

```bash
cd locust-performance-testing
pip install -r requirements.txt
python -m locust -f locustfile.py
```

Open your browser:

```
http://localhost:8089
```

Configuration

- Users: 10
- Spawn Rate: 2

---

## 📈 Performance Report


### Total Requests per Second

![Locust rps](./screenshots/locust_rps.png)

---
### Response Times

![Locust response](./screenshots/locust_response_time.png)

---

### Failure Rate

![Locust Failure Report](./screenshots/locust_failure_rate.png)

Failure Rate:
Most requests completed successfully.
Some failures were caused by authentication (401 Unauthorized) or temporary network connectivity issues during stress testing.

---

## 👨‍💻 Author

Bai, Chen-Liang

Department of Mathematics
Information Mathematics Program

Fu Jen Catholic University

GitHub:
https://github.com/balla930510-cmd/api-automation-testing

Email:
balla930510@gmail.com

---

## 📄 License

This project is created for learning and portfolio purposes.

Copyright © 2026 Bai Chen-Liang. All rights reserved.