# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time


# def setup_function(function):
#     global driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.com")

# def teardown_function(function):   
#     driver.quit()


# @pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
# def test_google_search(set_up_and_tear_down, search_term):
#     driver = set_up_and_tear_down 

#     search_box = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
#     )

#     search_box.send_keys(search_term)
#     search_box.submit()  
#     time.sleep(2)  
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")

def teardown_function(function):
    driver.quit()

@pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
def test_google_search(search_term):
    search_box = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )
    search_box.send_keys(search_term)
    search_box.submit()
    time.sleep(2)

