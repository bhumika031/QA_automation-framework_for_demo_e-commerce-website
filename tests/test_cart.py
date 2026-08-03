import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.smoke
def test_cart_contains_added_product(driver):
    
    logger.info("Start testing cart contained product")

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

    items = cart_page.get_item_names()

    assert "Sauce Labs Backpack" in items


@pytest.mark.regression
def test_cart_item_count(driver):
    
    logger.info("Start testing cart item counts ")

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

    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory_page.open_cart()

    assert cart_page.get_item_count() == 2


@pytest.mark.regression
def test_remove_product_from_cart(driver):
    
    logger.info("Start testing removing product from cart")

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

    cart_page.remove_product(
        "Sauce Labs Backpack"
    )

    assert cart_page.get_item_count() == 0