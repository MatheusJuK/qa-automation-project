from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")

    def checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(*self.CONTINUE_BUTTON)
    
    def wait_for_cart_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart")
        )