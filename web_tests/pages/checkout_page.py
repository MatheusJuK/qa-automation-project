from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.type(*self.FIRST_NAME, first_name)
        self.type(*self.LAST_NAME, last_name)
        self.type(*self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
            self.click(*self.CONTINUE_BUTTON)
            self.wait.until(EC.url_contains("checkout-step-two"))
        except:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            self.wait.until(EC.url_contains("checkout-step-one"))

    def finish_checkout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
            self.click(*self.FINISH_BUTTON)
            self.wait.until(EC.url_contains("checkout-complete"))
        except:
            self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
            self.wait.until(EC.url_contains("checkout-step-two"))
            self.click(*self.FINISH_BUTTON)
            self.wait.until(EC.url_contains("checkout-complete"))

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MESSAGE)
    
    def cancel_checkout(self):
        self.click(*self.CANCEL_BUTTON)
        
    