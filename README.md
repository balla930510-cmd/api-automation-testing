# API Automation & Performance Testing

![API Tests CI](https://github.com/balla930510-cmd/api-automation-testing/actions/workflows/api-test.yml/badge.svg)
![API Release](https://github.com/balla930510-cmd/api-automation-testing/actions/workflows/release.yml/badge.svg)

> Python-based API Automation Testing Framework featuring functional testing,
> Barcode Payment business scenarios, CI/CD automation, HTML test reporting,
> and performance testing with Locust.

This project demonstrates how to design, maintain, and execute an API automation
framework using **Python, Pytest, Requests, Flask, GitHub Actions, and Locust**.

## 🎯 Project Highlights

This project demonstrates practical QA automation skills including:

- API functional testing
- Business scenario testing
- Positive / Negative / Boundary testing
- API response validation
- Test data management
- Pytest fixture and parameterization
- API client abstraction
- CI/CD integration
- Automated HTML test reporting
- Performance testing with Locust

## 🧠 Skills Demonstrated

- API Test Automation
- Test Case Design
- Business Logic Validation
- Positive / Negative / Boundary Testing
- Pytest Fixture Design
- Parameterized Testing
- Test Data Management
- API Client Abstraction
- CI/CD Integration
- HTML Test Reporting
- Performance Testing
- Failure Analysis and Debugging

## Features

### API Automation

✔ REST API Automation

✔ CRUD API Testing

✔ Positive / Negative / Boundary Testing

✔ HTTP Status Code Validation

✔ Response Data Validation

✔ Modular API Client

✔ Pytest Fixtures

✔ Parameterized Testing

✔ Test Data Management

✔ Test Isolation

### Business Scenario Testing

✔ Barcode Payment API Testing

✔ Barcode Scan Validation

✔ Payment Validation

✔ Duplicate Payment Validation

✔ Payment Status Testing

### Reporting & CI/CD

✔ HTML Test Report with pytest-html

✔ GitHub Actions CI

✔ Automated Test Report Artifact

✔ CI/CD Workflow

✔ Automated GitHub Release

✔ Git-based Version Control

### Performance Testing

✔ Performance Testing with Locust

✔ Response Time Monitoring

✔ Requests Per Second (RPS)

✔ Failure Rate Monitoring

✔ Concurrent User Load

## 🛠 Technologies

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| HTTP Client | Requests |
| Test Framework | Pytest |
| Mock API | Flask |
| Test Architecture | API Client / Fixtures |
| Test Data | Pytest Fixtures / Parameterization |
| Test Reporting | pytest-html |
| Performance | Locust |
| CI/CD | GitHub Actions |
| Version Control | Git / GitHub |

## 📂 Project Structure

```text
API_Testing/
│
├── .github/
│   └── workflows/
│       ├── api-test.yml
│       └── release.yml
│
├── api/
│   └── api_client.py
│
├── app/
│   └── main.py
│
├── config/
│   └── config.py
│
├── data/
│   └── test_data.py
│
├── tests/
│   ├── test_barcode_scan.py
│   ├── test_create_user.py
│   ├── test_delete_user.py
│   ├── test_get_user.py
│   ├── test_parameter.py
│   ├── test_payment.py
│   ├── test_payment_status.py
│   └── test_update_user.py
│
├── reports/
│   └── screenshot/report.png
│
├── screenshots/
│   ├── locust_failure_rate.png
│   ├── locust_response_time.png
│   └── locust_rps.png
│
├── locust-performance-testing/
│   ├── locustfile.py
│   ├── requirements.txt
│   └── README.md
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

Generated reports and temporary files are excluded from source control through .gitignore.

## 🏗 Architecture

### API Automation

```text
            Pytest Test Cases
                     │
                     ▼
             Pytest Fixtures
                     │
                     ▼
                API Client
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
User REST API                 Flask Mock 
                                  │
                                  ▼
                          Barcode Payment API
                                  │
                                  ▼
                          Response Validation
                                  │
                                  ▼
                              Assertions
                                  │
                                  ▼
                             pytest-html
                                  │
                                  ▼
                              HTML Report
 ```                                
## 💳 Barcode Payment Testing

The project includes a Flask-based Mock Barcode Payment API to simulate
real-world payment business scenarios and validate payment-related business logic.

### Payment Flow

```text
Barcode Scan
     │
     ▼
Validate Barcode
     │
     ├── Invalid ───────► FAILED
     │
     ▼
Payment Request
     │
     ▼
Validate Amount
     │
     ├── Invalid ───────► FAILED
     │
     ▼
Check Barcode Status
     │
     ├── Already Used ──► FAILED
     │
     ▼
Create Payment
     │
     ▼
  SUCCESS
     │
     ▼
Transaction ID
```
## Test Scenarios
| Scenario | Expected Result |
| -------- | --------------- |
| Valid barcode | SUCCESS |
| Invalid barcode | INVALID_BARCODE |
| Expired barcode | BARCODE_EXPIRED |
| Already used barcode | BARCODE_ALREADY_USED |
| Amount = 0 | INVALID_AMOUNT |
| Negative amount | INVALID_AMOUNT |
| Invalid amount type | INVALID_AMOUNT |
| Missing amount | AMOUNT_REQUIRED |
| Duplicate payment | BARCODE_ALREADY_USED |
| Payment status lookup | SUCCESS / NOT_FOUND |

### Test Design Techniques

The test suite covers:

- Positive testing
- Negative testing
- Boundary value testing
- Invalid input validation
- Missing field validation
- Business rule validation
- Duplicate transaction validation
- HTTP status code validation
- Response body validation

Examples include validating zero and negative payment amounts,
invalid barcode values, expired barcodes, duplicate payments,
and missing required fields.

Pytest parameterization is used to execute multiple test scenarios
with different input data while reducing duplicated test code.


## 🚀 API Automation Testing
### Test Coverage

The API automation suite currently covers the following operations:

| Method | Test Coverage |
| ------ | ------------- |
| GET |	Retrieve user data |
| POST | Create a new user |
| PUT |	Update user data |
| DELETE | Delete user |
---


###  API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/users?page=2 | Retrieve user list |
| POST | /api/users | Create a new user |
| PUT | /api/users/2 | Update user |
| DELETE | /api/users/2 | Delete user |
---
## ✅ Test Results

| Metric | Result |
|--------|--------|
| Total Tests | 21 |
| Passed | 21 |
| Failed | 0 |
| Pass Rate | 100% |

## 📄 HTML Test Report

The project uses pytest-html to generate a self-contained HTML test report.

```bash
pytest --html=reports/report.html --self-contained-html
```
The generated report contains:

- Total test cases
- Passed tests
- Failed tests
- Error information
- Test execution duration
- Test case details

The report is also automatically generated during GitHub Actions CI
and uploaded as a workflow artifact.

### Report Screenshot

![Pytest HTML Report](reports/screenshot/report.png)
---

## 🔄 Continuous Integration

The project uses GitHub Actions to automatically execute the API test
suite on every push and pull request targeting the `main` branch.

### CI Workflow

The workflow is defined in:

```text
.github/workflows/api-test.yml

```
The workflow automatically:

- Checks out the repository
- Sets up Python 3.12
- Installs project dependencies
- Starts the Flask Mock API
- Runs the Pytest test suite
- Generates a self-contained HTML test   report
- Uploads the report as a GitHub Actions artifact
- Preserves the report even when tests fail

### CI Test Workflow
```text
       Push / Pull Request
                │
                ▼
         GitHub Actions CI
                │
                ▼
        Checkout Repository
                │
                ▼
         Setup Python 3.12
                │
                ▼
       Install Dependencies
                │
                ▼
       Start Flask Mock API
                │
                ▼
            Run Pytest
                │
                ▼
       Generate HTML Report
                │
                ▼
      Upload Report Artifact
```

## 📦 CI Test Report Artifact

The generated HTML report is uploaded to GitHub Actions as a workflow artifact.
```text
           GitHub Actions
                 │
                 ▼
               pytest
                 │
                 ▼
         reports/report.html
                 │
                 ▼
           Upload Artifact
                 │
                 ▼
           api-test-report
```
The artifact allows test results to be inspected after the CI workflow completes without committing generated reports to the repository.

## 🚀 Continuous Delivery

The project includes a GitHub Actions release workflow for automated GitHub Releases.

### CD Workflow

The release workflow is defined in:

```text
.github/workflows/release.yml
```
The release pipeline:

- Is triggered manually through GitHub Actions
- Sets up Python 3.12
- Installs project dependencies
- Runs the API test suite
- Creates a GitHub Release when all tests pass

### Release Flow
```text
Manual Release Trigger
        │
        ▼
GitHub Actions CD
        │
        ▼
Setup Python 3.12
        │
        ▼
Install Dependencies
        │
        ▼
   Run Pytest
        │
        ▼
    Test Pass
        │
        ▼
Create GitHub Release
```

## ⚡ Performance Testing (Locust)

Locust is used to evaluate the performance of a public REST API,
while the Flask Mock API is used for functional and business scenario testing.


### Target API

```
https://reqres.in
```

### Test Scenario

The performance test evaluates API response time,
throughput, failure rate, and behavior under concurrent load.

Target endpoints:

- GET /api/users?page=2
- POST /api/users

Performance metrics include:

- Requests Per Second (RPS)
- Response Time
- Failure Rate
- Concurrent User Load
###  Run Locust
Navigate to the performance testing directory:
```bash
cd locust-performance-testing
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Start Locust:
```bash
python -m locust -f locustfile.py
```

Open the Locust Web UI:

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

Performance results may vary depending on external API behavior, network conditions, and test load.

---
## 🔧 Installation
1. Clone the repository
```bash
git clone https://github.com/balla930510-cmd/api-automation-testing.git
```
2. Navigate to the project
```bash
cd api-automation-testing
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
## ▶️ Run Tests

### 1. Start the Mock API

In Terminal 1:

```bash
python app/main.py
```
The API will be available at:

```text
http://127.0.0.1:5000
```
### 2. Run the test suite
In terminal 2:
```bash
pytest -v
```

### Run all tests
```bash
pytest
```

### Generate HTML test report:
```bash
pytest --html=reports/report.html --self-contained-html
```
## 💻 Test Environment

| Item | Local | CI |
|------|-------|----|
| OS | Windows 11 | Ubuntu |
| Python | 3.13.9 | 3.12 |
| Test Framework | Pytest | Pytest |
| API Library | Requests | Requests |
| HTML Report | pytest-html | pytest-html |
| Performance | Locust | — |
| CI/CD | — | GitHub Actions |
---


## 👨‍💻 Author

Bai, Chen-Liang

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