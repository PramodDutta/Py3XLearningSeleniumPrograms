from selenium import webdriver
def test_sample():
    # Selenium 3 - Not much used now
    # driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    # driver.get("https://app.vwo.com")


    # Selenium 4 ( Selenium manager) - who will download the driver by itself)
    driver = webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"