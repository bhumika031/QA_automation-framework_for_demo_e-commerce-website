import pytest

from pages.login_page import LoginPage
from utilities.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.smoke
def test_valid_login(driver):
    logger.info("Start testing valid login")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory.html" in driver.current_url


@pytest.mark.regression
def test_invalid_username(driver):
    logger.info("Start testing invalid login")

    login_page = LoginPage(driver)

    login_page.login(
        "invalid_user",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


@pytest.mark.regression
def test_empty_username(driver):
    logger.info("Start testing empty username")

    login_page = LoginPage(driver)

    login_page.login(
        "",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert error == "Epic sadface: Username is required"


@pytest.mark.regression
def test_empty_password(driver):
    logger.info("Start testing empty password")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        ""
    )

    error = login_page.get_error_message()

    assert error == "Epic sadface: Password is required"


@pytest.mark.regression
def test_locked_out_user(driver):
    logger.info("Start testing locked out user")

    login_page = LoginPage(driver)

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert "locked out" in error.lower()