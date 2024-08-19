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


@pytest.mark.positive
def test_vwo_login_16():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    element = driver.find_element(By.ID,"this_id_doesnt_exist")
    # 'status': 404
    # no such element , Unable to locate element
    # NoSuchElementException
    print("End of the program")

    time.sleep(3)





