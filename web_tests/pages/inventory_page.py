from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InventoryPage(BasePage):
    
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BIKE = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_TO_CART_ALL = (By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def add_products_to_cart(self):
        self.click(*self.ADD_TO_CART_BACKPACK)
        self.click(*self.ADD_TO_CART_BIKE)
        self.click(*self.ADD_TO_CART_TSHIRT)
        self.click(*self.ADD_TO_CART_JACKET)
        self.click(*self.ADD_TO_CART_ONESIE)
        self.click(*self.ADD_TO_CART_ALL)

    def go_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
            self.click(*self.CART_BUTTON)
            self.wait.until(EC.url_contains("cart"))
        except:
            self.driver.get("https://www.saucedemo.com/cart.html")
            self.wait.until(EC.url_contains("cart"))

        