# E-Commerce Website Testing

A fresher-friendly QA practice project for testing the [SauceDemo](https://www.saucedemo.com/) demo shop with manual test cases and Python, Selenium WebDriver, and Pytest.

## Scope

- Login with valid, invalid, and empty credentials
- Product listing, product images, and price sorting
- Add/remove products and verify the cart badge
- Complete checkout and verify the order confirmation
- Record manual test results and defects

SauceDemo does not provide a product search field; sorting is covered instead.
This is a UI test project, not a test of SauceDemo's internal database.

## Requirements

- Python 3.10 or later
- Google Chrome
- Internet access to reach SauceDemo

## Setup and run

From this folder, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the full browser suite:

```powershell
python -m pytest
```

Pytest opens Chrome in headless mode by default and writes a self-contained HTML
report to `pytest-report.html`. Selenium Manager resolves the ChromeDriver
version; the first run may need internet access. To see the browser while tests
run, set `HEADLESS=0` in the environment before running Pytest. Failed tests
include an embedded screenshot in the HTML report.

The test URL and credentials can be overridden with `SAUCEDEMO_BASE_URL`,
`SAUCEDEMO_USERNAME`, and `SAUCEDEMO_PASSWORD`. Defaults are SauceDemo's public
demo URL and `standard_user` / `secret_sauce`.

Examples:

```powershell
$env:HEADLESS = "0"
python -m pytest tests\test_checkout.py
```

## Project structure

```text
.
├── conftest.py
├── docs/
│   ├── defect-report-template.md
│   └── manual-test-cases.csv
├── pytest.ini
├── requirements.txt
└── tests/
    ├── conftest.py
    ├── test_cart.py
    ├── test_checkout.py
    ├── test_login.py
    └── test_products.py
```

## Manual testing workflow

1. Review the cases in `docs/manual-test-cases.csv`.
2. Execute each case against SauceDemo and fill in Actual Result, Status, and
   Execution Date.
3. Record reproducible failures using `docs/defect-report-template.md`.
4. Run the automated suite after changes and review the HTML report.

The manual cases are starting examples. Add environment, build/version, and
evidence details when you execute them. Report only defects you reproduce.

## SQL practice

`sql/sample_validation.sql` is an optional, standalone SQLite exercise for
practising product/order data validation. It does not connect to or validate
SauceDemo's private backend.

## Interview/resume note

Describe only the test cases you actually executed and tools you genuinely
used. The public demo site can change or be unavailable, so record the date and
environment of each run.
