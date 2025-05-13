import pytest
import time
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    def test_validation(self):
        self.driver.find_element(By.ID,value="login2").click()
        username=read_config.get_config("login credentials","uname")
        passw=read_config.get_config("login credentials","passw")
        self.driver.find_element(By.ID,value="loginusername").send_keys(username)
        self.driver.find_element(By.ID,value="loginpassword").send_keys(passw)
        self.driver.find_element(By.XPATH,value="//button[text()='Log in']").click()
        time.sleep(5)
        # assert self.driver.find_element