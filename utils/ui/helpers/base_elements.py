import allure

from selenium.webdriver.common.by import By
from utils.ui.Locators import LocatorCodeMirror


class Table:
    def __init__(self, app, table_locator):
        self.app = app
        self.locator = table_locator
        self._table_element = None
        self._columns = None
        self._columns_dict = dict()
        self.updated = True
        self._data = None

    @allure.step('Обновить таблицу')
    def update(self):
        self._table_element = self.app.base.find_element_with_wait(self.locator)
        self._columns = [elem.text for elem in self._table_element.find_elements(By.TAG_NAME, "th")]
        for i, v in enumerate(self._columns):
            self._columns_dict[v] = i
        self.updated = False

    def table_element(self):
        if self.updated:
            self.update()
        return self._table_element

    @allure.step('Получить заголовки всех столбцов списком')
    def columns(self):
        if self.updated:
            self.update()
        return self._columns

    @allure.step('Получить заголовки всех столбцов словарем')
    def columns_dict(self):
        if self.updated:
            self.update()
        return self._columns_dict

    @allure.step('Получить все строки таблицы')
    def get_rows(self):
        return self.table_element().find_elements(By.TAG_NAME, "tr")

    @allure.step('Получить все данные из строки таблицы')
    def get_row_data(self, row):
        res = dict()
        for i, v in enumerate(row.find_elements(By.TAG_NAME, "td")):
            res[self.columns()[i]] = v.text
        return res

    @allure.step('Получить все данные из всех строк таблицы')
    def data(self) -> list:
        rows = self.get_rows()
        self._data = [self.get_row_data(row) for row in rows[1:]]
        return self._data

    @allure.step('Найти строку по значению')
    def find_by_value(self, column, value):
        for row in self.data():
            if row[column] == value:
                return row
        return None


class CodeMirror:

    def __init__(self, app):
        self.app = app
        self._code_mirror = None
        self.updated = True

    def update(self):
        self._code_mirror = self.app.base.find_element_with_wait(LocatorCodeMirror.CODE_MIRROR)
        self.updated = False

    @property
    def code_mirror(self):
        if self.updated:
            self.update()
        return self._code_mirror

    @allure.step('Очистить поле для ввода')
    def clear(self):
        self.app.wd.execute_script("arguments[0].CodeMirror.setValue('');", self.code_mirror)

    def send_keys(self, text):
        self.app.wd.execute_script(f'arguments[0].CodeMirror.setValue("{text}");', self.code_mirror)
