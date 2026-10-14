import os

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("driver")
    if browser is not None:
        extras = getattr(report, "extras", [])
        extras.append(
            pytest_html.extras.png(
                browser.get_screenshot_as_png(), name="Failure screenshot"
            )
        )
        report.extras = extras


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com/"),
        help="Base URL of the e-commerce application under test",
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def credentials():
    return {
        "username": os.getenv("SAUCEDEMO_USERNAME", "standard_user"),
        "password": os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce"),
    }


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "1").lower() not in {"0", "false", "no"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)
    yield browser
    browser.quit()
