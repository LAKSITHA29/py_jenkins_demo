# import pytest
# from selenium.webdriver.common.by import By

# @pytest.mark.usefixtures("setup_and_teardown")
# def test_with_valid_product(setup_and_teardown):
#     driver = setup_and_teardown  
#     search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("HP")
#     sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
#     expected = "HP LP3065"
#     text = driver.find_element(By.XPATH, value="//a[contains(text(),'HP LP3065')]").text
#     assert text == expected

# @pytest.mark.usefixtures("setup_and_teardown")
# def test_with_invalid_product(setup_and_teardown):
#     driver = setup_and_teardown  
#     search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("hee")
#     sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
#     expected = "There is no product that matches the search criteria."
#     text = driver.find_element(By.XPATH, value="//*[@id='content']/p[2]").text
#     assert text == expected

# @pytest.mark.usefixtures("setup_and_teardown")
# def test_with_empty_product(setup_and_teardown):
#     driver = setup_and_teardown  
#     search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("")
#     sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
#     expected = "There is no product that matches the search criteria."
#     text = driver.find_element(By.XPATH, value="//*[@id='content']/p[2]").text
#     assert text == expected

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
def test_google_search(set_up_and_tear_down, search_term):
    driver = set_up_and_tear_down 

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )

    search_box.send_keys(search_term)
    search_box.submit()  
    time.sleep(2)  