from web_tests.driver.driver_factory import create_driver

def test_open_page():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
    finally:
        driver.quit()