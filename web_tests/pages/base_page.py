from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, locator))
        )
    
    def click(self, by, locator):
        self.find(by, locator).click()
    
    def type(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by, locator):
        return self.find(by, locator).text