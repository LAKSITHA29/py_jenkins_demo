# import pytest
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from utils import excelReader

# @pytest.mark.parametrize("username,password",excelReader.get_data("C:\\PYTHON_SELENIUM\\pytest_folder\\Excel_Files\\loginData.xlsx","Sheet1"))
# class TestLogin1:
#     def test_validlogin1(self,username,password):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://demoblaze.com/index.html")
#         self.driver.find_element(By.ID,value="login2").click()
#         time.sleep(5)
#         self.driver.find_element(By.ID,value="loginusername").send_keys("")
#         time.sleep(5)
#         self.driver.find_element(By.ID,value="loginpassword").send_keys("")
#         time.sleep(5)
#         self.driver.find_element(By.XPATH,value="//button[text()='Log in']").click()
#         time.sleep(5)
#         assert self.driver.find_element(By.ID,value="logout2").is_displayed()

import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from utils import excelReader

@pytest.mark.parametrize("username, password,expected",excelReader.get_data("C:\\PYTHON_SELENIUM\\pytest_folder\\Excel_Files\\loginData.xlsx", "Sheet1"))
class TestLogin1:
    def test_validlogin1(self, username, password,expected):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")
        self.driver.find_element(By.ID, value="login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID, value="loginusername").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID, value="loginpassword").send_keys(password)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//button[text()='Log in']").click()
        time.sleep(5)

        if expected == "Valid":
            assert self.driver.find_element(By.ID, value="logout2").is_displayed()
        elif expected== "Invalid":
            alert = self.driver.switch_to.alert
            assert alert.text == "Wrong password."
            alert.accept()

        # assert self.driver.find_element(By.ID, value="logout2").is_displayed()
