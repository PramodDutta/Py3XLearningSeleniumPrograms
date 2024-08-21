# Actions and Windows, and Iframe.
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_021_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    # first_name.send_keys("thetestingacademy")
    # THETESTINGACADEMY

    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"the testing academy").key_up(Keys.SHIFT).perform()




    time.sleep(10)
    driver.quit()