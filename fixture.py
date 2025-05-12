import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

# def test_with_valid_product():
#     search=driver.find_element(By.XPATH,value="//input[@name='search']").send_keys("HP")
#     sbtn=driver.find_element(By.XPATH,value="//span[@class='input-group-btn']").click()
#     expect="HP LP3065"
#     text= driver.find_element(By.XPATH,value="//a[contains(text(),'HP LP3065')]").text()
#     assert text.__eq__(except)

def test_with_valid_product(test_setup_and_teardown):
    search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("HP")
    sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
    expected = "HP LP3065"
    text = driver.find_element(By.XPATH, value="//a[contains(text(),'HP LP3065')]").text
    assert text == expected

def test_with_invalid_product(test_setup_and_teardown):
    search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("hee")
    sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
    expected = "There is no product that matches the search criteria."
    text = driver.find_element(By.XPATH, value="//*[@id='content']/p[2]").text
    assert text == expected

def test_with_empty_product(test_setup_and_teardown):
    search = driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("")
    sbtn = driver.find_element(By.XPATH, value="//span[@class='input-group-btn']").click()
    expected = "There is no product that matches the search criteria."
    text = driver.find_element(By.XPATH, value="//*[@id='content']/p[2]").text
    assert text == expected