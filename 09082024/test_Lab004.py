import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    chrome_options = Options()
    chrome_options.add_extension("/Users/promode/Downloads/adblock.crx")
    chrome_options.add_argument("--page-load-strategy=eager")

    # You have to start the Chrome with an extension
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
