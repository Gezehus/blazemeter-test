from BaseApp import BasePage
from selenium.webdriver.common.by import By

from pages.WizardPage import WizardPageHelper


class RegistrationPageLocators:
    LOCATOR_FIRST_NAME_FIELD = (By.ID, 'firstName')
    LOCATOR_LAST_NAME_FIELD = (By.ID, 'lastName')
    LOCATOR_EMAIL_FIELD = (By.ID, 'email')
    LOCATOR_COMPANY_FIELD = (By.ID, 'user.attributes.company')
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")


class RegistrationPageHelper(BasePage):
    URL = 'registration'

    def enter_first_name(self, word):
        self.find_element(RegistrationPageLocators.LOCATOR_FIRST_NAME_FIELD).send_keys(word)

    def enter_last_name(self, word):
        self.find_element(RegistrationPageLocators.LOCATOR_LAST_NAME_FIELD).send_keys(word)

    def enter_email(self, word):
        self.find_element(RegistrationPageLocators.LOCATOR_EMAIL_FIELD).send_keys(word)

    def enter_company(self, word):
        self.find_element(RegistrationPageLocators.LOCATOR_COMPANY_FIELD).send_keys(word)

    def click_on_submit_button(self):
        self.find_element(RegistrationPageLocators.LOCATOR_SUBMIT_BUTTON, time=2).click()
        self.wait_until_get_to_url(WizardPageHelper.URL)

    def is_submit_button_displayed(self):
        return self.find_element(RegistrationPageLocators.LOCATOR_SUBMIT_BUTTON, time=2).is_displayed()
