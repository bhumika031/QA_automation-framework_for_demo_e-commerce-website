from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

class CartPage:

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(__name__)

    def get_item_names(self):
        self.logger.info("Getting items from the cart")

        elements = self.driver.find_elements(*self.ITEM_NAMES)

        return [element.text for element in elements]

    def get_item_count(self):

        return len(
            self.driver.find_elements(*self.CART_ITEMS)
        )

    def remove_product(self, product_name):
        
        self.logger.info("Removing product from cart")

        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='cart_item']"
            "//button"
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def click_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def continue_shopping(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()