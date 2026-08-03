import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_logout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory.html" in driver.current_url

    inventory_page.logout()

    assert "saucedemo.com" in driver.current_url

    assert login_page.is_login_page_displayed()