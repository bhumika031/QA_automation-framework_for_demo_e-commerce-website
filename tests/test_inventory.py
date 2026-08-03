import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture
def logged_in(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    return InventoryPage(driver)


@pytest.mark.smoke
def test_inventory_page_displayed(logged_in):
    
    logger.info("Start testing inventory page is displayed or not ")

    assert logged_in.get_page_title() == "Products"


@pytest.mark.regression
def test_products_are_displayed(logged_in):
    
    logger.info("Start testing product are displayed or not ")

    products = logged_in.get_product_names()

    assert len(products) > 0


@pytest.mark.regression
def test_add_product_to_cart(logged_in):
    
    logger.info("Start testing adding products to cart ")

    logged_in.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert logged_in.get_cart_count() == 1


@pytest.mark.regression
def test_remove_product_from_cart(logged_in):
    
    logger.info("Start testing removing product from cart")

    logged_in.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert logged_in.get_cart_count() == 1

    logged_in.remove_product_from_cart(
        "Sauce Labs Backpack"
    )

    assert logged_in.get_cart_count() == 0


@pytest.mark.regression
def test_sort_products_low_to_high(logged_in):
    logger.info("Start testing sort products low to high")

    logged_in.sort_by("lohi")

    prices = logged_in.get_product_prices()

    assert prices == sorted(prices)