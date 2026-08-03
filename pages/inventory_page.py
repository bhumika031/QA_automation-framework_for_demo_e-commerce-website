from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(__name__)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).text

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(element.text.replace("$", "")) for element in elements]

    def add_product_to_cart(self, product_name):
        
        self.logger.info("Adding product to cart")

        product = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[text()='{product_name}']"
                    "/ancestor::div[@class='inventory_item']"
                    "//button"
                )
            )
        )

        product.click()

    def remove_product_from_cart(self, product_name):
        
        self.logger.info("Removing product from cart")

        product = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[text()='{product_name}']"
                    "/ancestor::div[@class='inventory_item']"
                    "//button"
                )
            )
        )

        product.click()

    def get_cart_count(self):

        elements = self.driver.find_elements(*self.CART_BADGE)

        if not elements:
            return 0

        return int(elements[0].text)

    def open_cart(self):
        
        self.logger.info("Opening cart")

        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()

    def sort_by(self, option):

        dropdown = self.wait.until(
            EC.visibility_of_element_located(self.SORT_DROPDOWN)
        )

        Select(dropdown).select_by_value(option)

    def open_menu(self):

        self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()

    def logout(self):

        self.open_menu()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        ).click()
        # print("After logout click:", self.driver.current_url)