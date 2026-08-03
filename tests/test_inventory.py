import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


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

    assert logged_in.get_page_title() == "Products"


@pytest.mark.regression
def test_products_are_displayed(logged_in):

    products = logged_in.get_product_names()

    assert len(products) > 0


@pytest.mark.regression
def test_add_product_to_cart(logged_in):

    logged_in.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert logged_in.get_cart_count() == 1


@pytest.mark.regression
def test_remove_product_from_cart(logged_in):

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

    logged_in.sort_by("lohi")

    prices = logged_in.get_product_prices()

    assert prices == sorted(prices)