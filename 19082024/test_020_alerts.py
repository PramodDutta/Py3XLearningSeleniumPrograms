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
from selenium.webdriver.common.alert import Alert


class TestAlerts:
    @pytest.mark.qa
    def test_alerts_tc1_normalalert(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
        element_prompt.click()
        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)  # 2
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        assert result == "You successfully clicked an alert"

    def test_alerts_tc2_confirm_alert(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
        element_prompt.click()
        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)  # 2
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        assert result == "You clicked: Ok"

    def test_alerts_tc3_jsprompt_alert(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
        element_prompt.click()
        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)  # 2
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        alert.send_keys("pramod")
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        assert result == "You entered: pramod"

    def test_checkbox(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        self.driver.maximize_window()
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkboxes[0].click()
        time.sleep(10)



