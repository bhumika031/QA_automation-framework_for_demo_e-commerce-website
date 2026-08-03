# Web Automation Testing Framework

A Python Selenium + Pytest web automation framework built for testing the [SauceDemo](https://www.saucedemo.com/) application.

## Overview

This project demonstrates a structured approach to web UI automation using:

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Page Object Model (POM)
- Logging
- Pytest HTML reports
- Automatic screenshots on test failure

## Features

- Valid and invalid login testing
- Locked-out user testing
- Inventory page validation
- Product listing and sorting
- Add/remove products from cart
- Cart validation
- Successful checkout
- Negative checkout scenarios
- Logout testing
- Product details testing
- Explicit waits
- Centralized browser fixture
- Logging
- Screenshot capture on failure
- HTML test reports

## Project Structure

```text
WebAutomationFramework/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── product_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│   └── test_product.py
│
├── utilities/
│   ├── logger.py
│   └── screenshot.py
│
├── logs/
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Design

The framework follows the **Page Object Model**.

- **Test files** describe what should be tested.
- **Page Object classes** contain how the application is interacted with.
- **conftest.py** centrally manages the browser fixture, setup, teardown, and failure screenshots.
- **utilities** contains reusable framework components such as logging and screenshots.

This separation improves maintainability and reduces code duplication.

## Test Coverage

### Login

- Valid login
- Invalid username
- Empty username
- Empty password
- Locked-out user

### Inventory

- Inventory page displayed
- Products displayed
- Add product to cart
- Remove product from cart
- Sort products

### Cart

- Added product appears in cart
- Cart item count
- Remove product from cart

### Checkout

- Successful checkout
- Missing first name
- Missing last name
- Missing postal code

### Logout

- Successful logout
- Login page verification after logout

### Product

- Open product details

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run with detailed output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_login.py -v
```

Show `print()` output:

```bash
pytest -s
```

Combine verbose output and print output:

```bash
pytest -v -s
```

## HTML Report

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report provides test results, failure details, duration, and metadata.

## Screenshots

When a test fails, the framework automatically captures a screenshot.

Screenshots are stored in:

```text
screenshots/
```

## Logging

Logging is centralized in:

```text
utilities/logger.py
```

Logs are written to:

```text
logs/automation.log
```

Example log messages:

```text
Creating Chrome WebDriver
Chrome browser started
SauceDemo opened
Entering username
Entering password
Clicking login button
Closing Chrome WebDriver
```

Generated logs are excluded from Git.

## Application Under Test

**SauceDemo**

https://www.saucedemo.com/

## Git

Generated files should not be committed to the repository.

The `.gitignore` excludes:

```gitignore
venv/
__pycache__/
*.pyc
.pytest_cache/
logs/
reports/
screenshots/
```

## Future Improvements

- Configuration files
- Test data management
- Environment-specific configuration
- CI/CD integration
- GitHub Actions
- Parallel execution
- Additional negative scenarios
- API testing integration

## Author

Python Selenium QA Automation Framework project created as a learning and portfolio project focused on professional QA automation practices.
