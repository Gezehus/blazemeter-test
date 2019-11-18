from BaseApp import BasePage
from selenium.webdriver.common.by import By


class EditAccountPageLocators:
    LOCATOR_FIRST_NAME_FIELD = (By.ID, 'firstName')
    LOCATOR_LAST_NAME_FIELD = (By.ID, 'lastName')
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOCATOR_ALERT = (By.XPATH, "//div[contains(@class, 'alert')]")


class EditAccountPageHelper(BasePage):
    URL = 'account'

    def enter_first_name(self, word):
        first_name = self.find_element(EditAccountPageLocators.LOCATOR_FIRST_NAME_FIELD)
        first_name.clear()
        first_name.send_keys(word)

    def enter_last_name(self, word):
        last_name = self.find_element(EditAccountPageLocators.LOCATOR_LAST_NAME_FIELD)
        last_name.clear()
        last_name.send_keys(word)

    def click_on_submit_button(self):
        self.find_element(EditAccountPageLocators.LOCATOR_SUBMIT_BUTTON, time=2).click()

    def get_alert_text(self):
        return self.find_element(EditAccountPageLocators.LOCATOR_ALERT, time=2).text
