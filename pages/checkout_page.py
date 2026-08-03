from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    CHECKOUT_OVERVIEW_TITLE = (By.CLASS_NAME, "title")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):

        element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):

        element = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )

        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code):

        element = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )

        element.clear()
        element.send_keys(postal_code)

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def click_finish(self):

        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def get_page_title(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.CHECKOUT_OVERVIEW_TITLE
            )
        ).text

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text