import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@pytest.mark.positive
def test_vwo_login_katalong_code():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    allure.attach(driver.get_screenshot_as_png(), name="Step1_Open_URL", attachment_type=AttachmentType.PNG)

    make_app = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_app.click()

    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    WebDriverWait(driver=driver, timeout=5).until(
        EC.url_contains("profile.php#login")
    )

    allure.attach(driver.get_screenshot_as_png(), name="Step2_Login_Page", attachment_type=AttachmentType.PNG)

    username = driver.find_element(By.CSS_SELECTOR, "#txt-username")
    password = driver.find_element(By.CSS_SELECTOR, "#txt-password")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")

    WebDriverWait(driver=driver, timeout=3).until(
        EC.element_to_be_clickable(((By.CSS_SELECTOR, "#btn-login")))
    )

    btn_login = driver.find_element(By.CSS_SELECTOR, "#btn-login")
    btn_login.click()

    allure.attach(driver.get_screenshot_as_png(), name="Step3_Login_Click", attachment_type=AttachmentType.PNG)

    WebDriverWait(driver=driver, timeout=15).until(
        EC.url_contains("#appointment")
    )


    h2_element = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")

    allure.attach(driver.get_screenshot_as_png(), name="Step3_Verify_h2_login", attachment_type=AttachmentType.PNG)
    assert h2_element.text == "Make Appointment"
