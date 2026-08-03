import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utilities.logger import get_logger

logger = get_logger(__name__)


def prepare_checkout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.open_cart()

    cart_page.click_checkout()

    return CheckoutPage(driver)


@pytest.mark.smoke
def test_successful_checkout(driver):
    
    logger.info("Start testing sucessful checkout")

    checkout_page = prepare_checkout(driver)

    checkout_page.enter_customer_information(
        "Bhumika",
        "Tester",
        "380001"
    )

    checkout_page.click_continue()

    assert (
        checkout_page.get_page_title()
        == "Checkout: Overview"
    )

    checkout_page.click_finish()

    assert (
        checkout_page.get_success_message()
        == "Thank you for your order!"
    )


@pytest.mark.regression
def test_checkout_without_first_name(driver):
    
    logger.info("Start testing without first name ")

    checkout_page = prepare_checkout(driver)

    checkout_page.enter_customer_information(
        "",
        "Tester",
        "380001"
    )

    checkout_page.click_continue()

    error = checkout_page.get_error_message()

    assert error == "Error: First Name is required"


@pytest.mark.regression
def test_checkout_without_last_name(driver):
    
    logger.info("Start testing checkout without last name ")

    checkout_page = prepare_checkout(driver)

    checkout_page.enter_customer_information(
        "Bhumika",
        "",
        "380001"
    )

    checkout_page.click_continue()

    error = checkout_page.get_error_message()

    assert error == "Error: Last Name is required"


@pytest.mark.regression
def test_checkout_without_postal_code(driver):
    
    logger.info("Start testing checkout without postal-code")

    checkout_page = prepare_checkout(driver)

    checkout_page.enter_customer_information(
        "Bhumika",
        "Tester",
        ""
    )

    checkout_page.click_continue()

    error = checkout_page.get_error_message()

    assert error == "Error: Postal Code is required"