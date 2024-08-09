import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)
    # driver.close()
    # # Close will close the current window or tab.
    # # session id != null( Invalid)
    # # It will not close the other tabs.

    time.sleep(60)
    driver.quit()
    # Close all the tabs.
    # session id == null






