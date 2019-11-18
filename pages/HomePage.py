from BaseApp import BasePage
from selenium.webdriver.common.by import By

from pages.RegistrationPage import RegistrationPageHelper


class HomePageLocators:
    LOCATOR_GET_STARTED_BUTTON = (By.CLASS_NAME, 'get_started_button')


class HomePageHelper(BasePage):

    def click_on_get_started_button(self):
        self.find_element(HomePageLocators.LOCATOR_GET_STARTED_BUTTON, time=2).click()
        self.wait_until_get_to_url(RegistrationPageHelper.URL)
