import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class BaseHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Поиск элемента')
    def find_element(self, *locator):
        wd = self.app.wd
        return wd.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, *locator):
        wd = self.app.wd
        return wd.find_elements(*locator)

    @allure.step('Поиск с ожиданием элемента')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self, 20).until(ec.visibility_of_element_located(locator),
                                             message='Не дождались отображения элемента')

    @allure.step('Ожидание отображения элемента')
    def wait(self, locator):
        WebDriverWait(self, 20).until(ec.visibility_of_element_located(locator),
                                      message='Не дождались отображения элемента')

    @allure.step('Клик по элементу')
    def click(self, locator):
        self.wait_for_click(locator)
        self.find_element(*locator).click()

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_click(self, locator):
        WebDriverWait(self, 45).until(ec.element_to_be_clickable(locator),
                                      message='Не дождались кликабельности элемента')

    @allure.step('Ожидание отображения элемента')
    def wait(self, locator):
        WebDriverWait(self, 20).until(ec.visibility_of_element_located(locator),
                                      message='Не дождались отображения элемента')

    @allure.step('Ввод текста в элемент')
    def send_keys(self, locator, text):
        self.click(locator)
        self.find_element(*locator).send_keys(text)

    @allure.step('Очистить поле ввода')
    def clear(self, locator):
        self.wait_for_click(locator)
        self.find_element(*locator).send_keys(Keys.CONTROL + "a")
        self.find_element(*locator).send_keys(Keys.DELETE)

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        self.wait(locator)
        return self.find_element(*locator).text
