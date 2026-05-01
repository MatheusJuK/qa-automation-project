from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")

    def checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(*self.CONTINUE_BUTTON)
    