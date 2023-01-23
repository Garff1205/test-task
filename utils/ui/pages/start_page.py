import random

import allure

from utils.ui.Locators import LocatorStart
from utils.ui.helpers.base_elements import Table, CodeMirror


class StartPage:

    def __init__(self, app):
        self.app = app
        self.main_table = Table(app, LocatorStart.RESULT_TABLE)
        self.your_db_table = Table(app, LocatorStart.YOUR_DB_TABLE)
        self.code_mirror = CodeMirror(app)

    @allure.step('Выполнить sql команду')
    def run_sql(self):
        self.app.base.click(LocatorStart.RUN_BUTTON)
        self.main_table.updated = True

    @allure.step('Выполнить запрос {query}')
    def execute_query(self, query):
        self.code_mirror.clear()
        self.code_mirror.send_keys(query)
        self.run_sql()

    @allure.step('Дождаться пока появится сообщение об успешном изменении таблицы')
    def wait_table_update(self):
        self.app.base.wait(LocatorStart.TABLE_UPDATE_MESSAGE)

    @allure.step('Проверить, что в строке где {column_name} = {column_value}, '
                 'значение {target_column} = {target_value}')
    def check_value_in_row(self, column_name, column_value, target_column, target_value) -> [bool, any]:
        row = self.main_table.find_by_value(column_name, column_value)
        if not row:
            return False, f'Строка с {column_name} = {column_value} не найдена'
        actual_value = row[target_column]
        return actual_value == target_value, actual_value

    @allure.step('Проверить, что в строке где {column_name} = {column_value}, '
                 'значения {row_dict}')
    def check_values_in_row(self, column_name: str, column_value: any, row_dict: dict) -> [bool, any]:
        row = self.main_table.find_by_value(column_name, column_value)
        bad = []
        if not row:
            return False, f'Строка с {column_name} = {column_value} не найдена'
        for column, value in row_dict.items():
            if value != row[column]:
                bad.append(f'{value} != {row[column]}')
        return not bad, bad

    @allure.step('Получить количество строк в таблице')
    def get_num_of_rows_in_table(self) -> int:
        return len(self.main_table.get_rows())-1

    @allure.step('Получить значение Number of Records')
    def get_number_of_records_value(self) -> int:
        text = self.app.base.get_text(LocatorStart.NUMBER_OF_RECORDS)
        return int(text.split(":")[-1].replace(" ", ""))

    @allure.step('Выбрать случайную запись из имеющихся в таблице и вернуть его CustomerID')
    def get_random_customer_id(self) -> int:
        row = random.choice(self.main_table.get_rows())
        return int(self.main_table.get_row_data(row)['CustomerID'])

    @allure.step('Получить количество записей указанных в инфо для талблицы {tablename}')
    def get_num_of_records(self, tablename) -> int:
        row = self.your_db_table.find_by_value('Tablename', tablename)
        return int(row['Records'])

    @allure.step('Восстановить таблицы поумолчанию')
    def restore_data(self):
        self.app.base.click(LocatorStart.RESTORE_BUTTON)
        self.app.base.accept_alert()
