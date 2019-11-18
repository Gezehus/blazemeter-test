import pytest
from selenium import webdriver

DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    driver.maximize_window()
    yield driver
    driver.quit()
