from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www-bm-qa-base.blazemeter.net/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_until_get_to_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url),
                                                      message=f"Can't get to url: {url}")

    def get_current_url(self):
        return self.driver.current_url

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def wait_for_time(self, seconds):
        time.sleep(seconds)
