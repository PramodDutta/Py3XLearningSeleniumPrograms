import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
@allure.title("Verify that URL changes when we click on the Make appointment button")
@allure.description(
    "Verify the URL changes")
def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # - Find the element the anchor tag
    # We need to find the unique attribute which can find the web element
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    # - Click on it
    make_appointment_element.click()

    # Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()






