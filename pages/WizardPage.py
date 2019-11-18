from BaseApp import BasePage
from selenium.webdriver.common.by import By

from pages.DashboardPage import DashboardPageHelper


class WizardPageLocators:
    LOCATOR_SKIP_BUTTON = (By.CLASS_NAME, 'skip')


class WizardPageHelper(BasePage):
    URL = 'welcome-wizard'

    def click_on_skip_button(self):
        self.find_element(WizardPageLocators.LOCATOR_SKIP_BUTTON, time=2).click()
        self.wait_until_get_to_url(DashboardPageHelper.URL)
