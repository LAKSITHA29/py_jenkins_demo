# # from pickle
# import pytest
# from selenium import webdriver

# @pytest.fixture()
# def setup_and_teardown():
#     #  global driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://tutorialsninja.com/demo/")
#     yield
#     driver.quit()
import pytest
from selenium import webdriver

# @pytest.fixture()
# def set_up_and_tear_down():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.com")  
#     yield driver  
#     driver.quit()

# @pytest.fixture(params=["chrome","firefox","edge"])
# def set_up_and_tear_down(request):
#     if request.param=="chrome":
#         driver=webdriver.Chrome()
#     elif request.param=="firefox":
#         driver=webdriver.Firefox()
#     elif request.param=="edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://www.google.com")  
#     request.cls.driver=driver
#     yield   
#     driver.quit()

# @pytest.fixture(params=["chrome", "firefox", "edge"])
# def set_up_and_tear_down(request):
#     browser = request.param

#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
    
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.com")
#     request.cls.driver=driver
#     yield 
#     driver.quit()

import pytest
from selenium import webdriver

import read_config
@pytest.fixture()
def set_up_and_tear_down(request):
    # browser=request.param
    browser=read_config.get_config("basic info","browser")
    driver=None
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    app_url=read_config.get_config("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()