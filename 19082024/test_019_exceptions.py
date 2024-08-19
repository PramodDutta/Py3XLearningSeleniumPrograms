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
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


@pytest.mark.positive
def test_vwo_login_16():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, "submit")))
        print("End of the program")
    except TimeoutException as see:
        # stale element reference
        print(see)
        print("TimeoutException occured!! , 10 Seconds Passed")
    finally:
        driver.quit()
