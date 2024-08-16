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
def test_vwo_login_select():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    element_select = driver.find_element(By.ID, "dropdown")
    select = Select(element_select)
    select.select_by_visible_text("Option 2")
    select.se("Option 2")

    time.sleep(10)





