from BaseApp import BasePage
from selenium.webdriver.common.by import By

from pages.EditAccountPage import EditAccountPageHelper


class UserMenuLocators:
    LOCATOR_HEADER = 'bzm-header.hydrated'
    LOCATOR_MENU = 'span.caret'
    LOCATOR_PERSONAL_SETTINGS = "a[href*='personal-settings"


class UserMenuPageHelper(BasePage):

    def open_user_menu(self):
        menu_button = self.driver.execute_script(
            f"""return document.querySelector("{UserMenuLocators.LOCATOR_HEADER}").shadowRoot.querySelector("{UserMenuLocators.LOCATOR_MENU}")""")
        menu_button.click()
        self.wait_for_time(2)

    def click_on_personal_settings(self):
        personal_settings = self.driver.execute_script(
            f"""return document.querySelector("{UserMenuLocators.LOCATOR_HEADER}").shadowRoot.querySelector("{UserMenuLocators.LOCATOR_PERSONAL_SETTINGS}")""")
        personal_settings.click()
        self.wait_until_get_to_url(EditAccountPageHelper.URL)
