import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.screenshot import take_screenshot
from utilities.logger import get_logger
from selenium.webdriver.chrome.options import Options




logger = get_logger(__name__)

@pytest.fixture
def driver(request):
    
    options = Options()
    options.add_argument("--incognito")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    
    logger.info("Creating Chrome WebDriver")

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service,
        options = options
    )

    driver.maximize_window()
    logger.info("Chrome browser started")

    driver.get(
        "https://www.saucedemo.com/"
    )
    logger.info("SauceDemo opened")
    

    yield driver

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            take_screenshot(
                driver,
                request.node.name
            )
    
    logger.info("Closing Chrome WebDriver")

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