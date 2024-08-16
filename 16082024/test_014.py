import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


@pytest.mark.positive
def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    # time.sleep(5) # This is Python Int who is waiting, Python Execution Halt.

    # A Condition to check the element
    # error_msg_element - comes after 5 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.ID, 'js-notification-box-msg'))
    )

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
