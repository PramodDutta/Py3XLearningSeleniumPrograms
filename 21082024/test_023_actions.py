# Actions and Windows, and Iframe.
import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_022_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # draggable
    element_to_hold = driver.find_element(By.ID, "draggable")

    # Create an ActionChains object
    actions = ActionChains(driver)

    actions.click_and_hold(on_element=element_to_hold).perform()










    time.sleep(10)
    driver.quit()