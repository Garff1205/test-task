import pytest
import random

from utils.ui.Queries import QueriesCustomers
from tests.ui.Data import NEW_ROW_DATA, UPDATED_ROW_DATA


@pytest.mark.task
def test_contact_name_address_match(fixture_open_page, name='Giovanni Rovelli', address="Via Ludovico il Moro 22"):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_ALL_DATA)
    is_right, value = fixture_open_page.start_page.check_value_in_row('ContactName', name, 'Address', address)
    assert is_right, f'Адрес не совпадает. Найденое значение {value}'


@pytest.mark.task
def test_num_of_rows_with_city(fixture_open_page, city='London', expected=6):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_BY_CITY(city))
    actual_rows = fixture_open_page.start_page.get_num_of_rows_in_table()
    assert actual_rows == expected, f'Количество строк не совпадает. Найдено {actual_rows} строк.'


@pytest.mark.task
def test_add_new_row_and_check(fixture_open_page, new_row=NEW_ROW_DATA):
    fixture_open_page.start_page.execute_query(QueriesCustomers.ADD_NEW_ROW(new_row))
    fixture_open_page.start_page.wait_table_update()
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_ALL_DATA)
    key = random.choice(list(new_row.keys()))
    is_ok, where_trouble = fixture_open_page.start_page.check_values_in_row(column_name=key,
                                                                            column_value=new_row[key],
                                                                            row_dict=new_row)
    assert is_ok, f"Найдены несоответствия в следующих значениях {where_trouble}"


@pytest.mark.task
def test_update_row_and_check(fixture_open_page, updated_row=UPDATED_ROW_DATA):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_ALL_DATA)
    customer_id = fixture_open_page.start_page.get_random_customer_id()
    fixture_open_page.start_page.execute_query(QueriesCustomers.UPDATE_ROW(updated_row,
                                                                           f'CustomerID = {customer_id}'))
    fixture_open_page.start_page.wait_table_update()
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_BY_CUSTOMER_ID(str(customer_id)))
    is_ok, where_trouble = fixture_open_page.start_page.check_values_in_row(column_name='CustomerID',
                                                                            column_value=str(customer_id),
                                                                            row_dict=updated_row)
    assert is_ok, f"Найдены несоответствия в следующих значениях {where_trouble}"


# Если следовать строго заданию, то теста test_num_of_rows_with_city достаточно, чтобы проверить условие 2.
# Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей.
# Но тут прям просится еще один тест на проверку значения "Number of Records:"
@pytest.mark.addition
def test_number_of_records_equal_to_table(fixture_open_page, city='London'):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_BY_CITY(city))
    actual_rows = fixture_open_page.start_page.get_num_of_rows_in_table()
    value_in_text = fixture_open_page.start_page.get_number_of_records_value()
    assert actual_rows == value_in_text, \
        f"Фактическое количество строк на странице {actual_rows} " \
        f"не совпадает с указанным наверху таблицы {value_in_text}"
