import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class BaseHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Find element')
    def find_element(self, *locator):
        wd = self.app.wd
        return wd.find_element(*locator)

    @allure.step('Find elements')
    def find_elements(self, *locator):
        wd = self.app.wd
        return wd.find_elements(*locator)

    @allure.step('Search with element display wait')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self, 20).until(ec.visibility_of_element_located(locator),
                                             message='Timeout exited. Element did not displayed')

    @allure.step('Element display wait')
    def wait(self, locator):
        WebDriverWait(self, 20).until(ec.visibility_of_element_located(locator),
                                      message='Timeout exited. Element did not displayed')

    @allure.step('Element click')
    def click(self, locator):
        self.wait_for_click(locator)
        self.find_element(*locator).click()

    @allure.step('Element clickable wait')
    def wait_for_click(self, locator):
        WebDriverWait(self, 45).until(ec.element_to_be_clickable(locator),
                                      message='Timeout exited. Element did not displayed')

    @allure.step('Send text to the element')
    def send_keys(self, locator, text):
        self.click(locator)
        self.find_element(*locator).send_keys(text)

    @allure.step('Clear entering field')
    def clear(self, locator):
        self.wait_for_click(locator)
        self.find_element(*locator).send_keys(Keys.CONTROL + "a")
        self.find_element(*locator).send_keys(Keys.DELETE)

    @allure.step('Get element text')
    def get_text(self, locator):
        self.wait(locator)
        return self.find_element(*locator).text

    @allure.step('Accept alert')
    def accept_alert(self):
        self.app.wd.switch_to.alert.accept()
