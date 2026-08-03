import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.regression
def test_open_product_details(driver):
    logger.info("Start testing open product details")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    product_page = ProductPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_page.open_product(
        "Sauce Labs Backpack"
    )

    assert (
        product_page.get_product_name()
        == "Sauce Labs Backpack"
    )

    assert product_page.get_product_description() != ""

    assert product_page.get_product_price() != ""