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
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@pytest.mark.positive
def test_vwo_login_16():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        # StaleElementReferenceException
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        # Document HTML might change  - refresh
        # element - textarea -> might be case that it is not available now.
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS

        # to fix the code we can add a logic
        textarea.send_keys("the testing academy")
        print("End of the program")
    except StaleElementReferenceException as see:
        # stale element reference
        print(see)
        print("Stale element reference")




    time.sleep(5)





