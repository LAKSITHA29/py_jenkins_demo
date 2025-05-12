import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('searchTerm',[('selenium'),('pytest'),('selenium Locators')])

def test_search(searchTerm):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.find_element(By.NAME,value="q").send_keys(searchTerm)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,value="gNO89b").click()
    time.sleep(5)
    driver.quit()

