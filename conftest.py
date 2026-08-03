import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.screenshot import take_screenshot


@pytest.fixture
def driver(request):

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    driver.maximize_window()

    driver.get(
        "https://www.saucedemo.com/"
    )

    yield driver

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            take_screenshot(
                driver,
                request.node.name
            )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )