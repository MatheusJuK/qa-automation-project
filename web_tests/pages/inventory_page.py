from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InventoryPage(BasePage):
    
    MENU = (By.CLASS_NAME, "bm-burger-button")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BIKE = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_TO_CART_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_TO_CART_ALL = (By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    FILTER = (By.CLASS_NAME, "product_sort_container")
    FILTER_PRICE_LOW_TO_HIGH = (By.XPATH, "//option[@value='lohi']")
    FILTER_PRICE_HIGH_TO_LOW = (By.XPATH, "//option[@value='hilo']")
    FILTER_NAME_A_TO_Z = (By.XPATH, "//option[@value='az']")
    FILTER_NAME_Z_TO_A = (By.XPATH, "//option[@value='za']")
    
    TWITTER_LINK = (By.XPATH, "//a[@href='https://twitter.com/saucelabs']")
    FACEBOOK_LINK = (By.XPATH, "//a[@href='https://www.facebook.com/saucelabs']")
    LINKEDIN_LINK = (By.XPATH, "//a[@href='https://www.linkedin.com/company/sauce-labs/']")

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
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
        self.click(*self.CART_BUTTON)
        self.wait.until(EC.url_contains("cart"))

    def sort_products(self, sort_option):
        self.click(*self.FILTER)
        self.click(*sort_option)
    
    def menu(self):
        self.click(*self.MENU)
        self.click(*self.ALL_ITEMS)
        self.click(*self.ABOUT)
        self.click(*self.RESET_APP_STATE)
        self.click(*self.MENU)
    
    def social_media_links(self):
        self.click(*self.TWITTER_LINK)
        self.click(*self.FACEBOOK_LINK)
        self.click(*self.LINKEDIN_LINK)
    
    def logout(self):
        self.click(*self.MENU)
        self.click(*self.LOGOUT_BUTTON)
        