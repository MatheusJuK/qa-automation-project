from web_tests.driver.driver_factory import create_driver

def test_open_page():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
    finally:
        driver.quit()

def test_login():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        username_input = driver.find_element("id", "user-name")
        password_input = driver.find_element("id", "password")
        login_button = driver.find_element("id", "login-button")
        
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        
        assert "Products" in driver.page_source
    finally:
        driver.quit()