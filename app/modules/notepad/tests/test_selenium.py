from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get("http://localhost:5000/")
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "email").click()
        driver.find_element(By.ID, "email").send_keys("user1@example.com")
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "submit").click()
        driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(9) .align-middle:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".text-dark").click()
        driver.find_element(By.CSS_SELECTOR, ".dropdown-menu").click()
        driver.find_element(By.LINK_TEXT, "Doe, John").click()
        driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(2)").click()

        try:

            pass

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_notepad_index()
