from web_tests.driver.driver_factory import create_driver
from web_tests.pages.login_page import LoginPage
from web_tests.pages.inventory_page import InventoryPage
from web_tests.pages.cart_page import CartPage
from web_tests.pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase_flow():
    driver = create_driver()
    
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    inventory_page.add_products_to_cart()

    inventory_page.go_to_cart()
    cart_page.wait_for_cart_page()
    
    assert "cart" in driver.current_url
    cart_page.checkout()

    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.wait_for_checkout_page()
    checkout_page.finish_checkout()

    success_message = checkout_page.get_success_message()
    assert success_message == "Thank you for your order!"

    driver.quit()