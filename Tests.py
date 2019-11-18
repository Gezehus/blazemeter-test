from pages.DashboardPage import DashboardPageHelper
from pages.EditAccountPage import EditAccountPageHelper
from pages.HomePage import HomePageHelper
from pages.RegistrationPage import RegistrationPageHelper
from pages.UserMenu import UserMenuPageHelper
from pages.WizardPage import WizardPageHelper

from utils.RandomStringGenerator import RandomGenerator

user = {'first_name': RandomGenerator.random_string(), 'last_name': RandomGenerator.random_string(),
        'email': RandomGenerator.random_email(), 'company': RandomGenerator.random_string()}

changed_user = {'first_name': RandomGenerator.random_string(), 'last_name': RandomGenerator.random_string()}


def test_go_to_registration(browser):
    home_page = HomePageHelper(browser)
    home_page.go_to_site()
    home_page.click_on_get_started_button()
    assert RegistrationPageHelper.URL in home_page.get_current_url()


def test_fill_in_registration_form(browser):
    registration_page = RegistrationPageHelper(browser)
    registration_page.enter_first_name(user['first_name'])
    registration_page.enter_last_name(user['last_name'])
    registration_page.enter_email(user['email'])
    registration_page.enter_company(user['company'])
    registration_page.click_on_submit_button()
    assert WizardPageHelper.URL in registration_page.get_current_url()


def test_skip_wizard(browser):
    wizard_page = WizardPageHelper(browser)
    wizard_page.click_on_skip_button()
    assert DashboardPageHelper.URL in wizard_page.get_current_url()


def test_change_name(browser):
    user_menu_page = UserMenuPageHelper(browser)
    user_menu_page.open_user_menu()
    user_menu_page.click_on_personal_settings()
    edit_account_page = EditAccountPageHelper(browser)
    edit_account_page.enter_first_name(changed_user['first_name'])
    edit_account_page.enter_last_name(changed_user['last_name'])
    edit_account_page.click_on_submit_button()
    assert 'Your account has been updated.' in edit_account_page.get_alert_text()
