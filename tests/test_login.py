import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory.html" in driver.current_url


@pytest.mark.regression
def test_invalid_username(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "invalid_user",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


@pytest.mark.regression
def test_empty_username(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert error == "Epic sadface: Username is required"


@pytest.mark.regression
def test_empty_password(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        ""
    )

    error = login_page.get_error_message()

    assert error == "Epic sadface: Password is required"


@pytest.mark.regression
def test_locked_out_user(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    error = login_page.get_error_message()

    assert "locked out" in error.lower()