from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")

    def checkout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
            self.click(*self.CHECKOUT_BUTTON)
            self.wait.until(EC.url_contains("checkout-step-one"))
        except:
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            self.wait.until(EC.url_contains("checkout-step-one"))

    