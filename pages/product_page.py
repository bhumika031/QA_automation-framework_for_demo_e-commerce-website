from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger


class ProductPage:

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(__name__)

    def open_product(self, product_name):
        
        self.logger.info(f"Open Product : {product_name}")

        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def get_product_description(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_DESCRIPTION)
        ).text

    def get_product_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_PRICE)
        ).text

    def back_to_products(self):

        self.wait.until(
            EC.element_to_be_clickable(self.BACK_TO_PRODUCTS)
        ).click()