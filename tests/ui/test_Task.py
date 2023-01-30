import pytest
import random

from utils.ui.Queries import QueriesCustomers
from tests.ui.Data import NEW_ROW_DATA, UPDATED_ROW_DATA, NEW_CATEGORY_DATA


@pytest.mark.task
def test_contact_name_address_match(fixture_open_page, name='Giovanni Rovelli', address="Via Ludovico il Moro 22"):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_ALL_DATA)
    is_right, value = fixture_open_page.start_page.check_value_in_row('ContactName', name, 'Address', address)
    assert is_right, f'Address does not matches. Value found {value}'


@pytest.mark.task
def test_num_of_rows_with_city(fixture_open_page, city='London', expected=6):
    fixture_open_page.start_page.restore_data()
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_BY_CITY(city))
    actual_rows = fixture_open_page.start_page.get_num_of_rows_in_table()
    assert actual_rows == expected, f'Number of rows does not matches. {actual_rows} rows found.'


@pytest.mark.task
def test_add_new_row_and_check(fixture_open_page, table='Customers', new_row=NEW_ROW_DATA):
    fixture_open_page.start_page.execute_query(QueriesCustomers.ADD_NEW_ROW(table, new_row))
    fixture_open_page.start_page.wait_table_update()
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_ALL_DATA)
    key = random.choice(list(new_row.keys()))
    is_ok, where_trouble = fixture_open_page.start_page.check_values_in_row(column_name=key,
                                                                            column_value=new_row[key],
                                                                            row_dict=new_row)
    assert is_ok, f"Found inconsistencies in the following values: {where_trouble}"


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
    assert is_ok, f"Found inconsistencies in following values: {where_trouble}"


@pytest.mark.addition
def test_number_of_records_equal_to_table(fixture_open_page, city='London'):
    fixture_open_page.start_page.execute_query(QueriesCustomers.GET_BY_CITY(city))
    actual_rows = fixture_open_page.start_page.get_num_of_rows_in_table()
    value_in_text = fixture_open_page.start_page.get_number_of_records_value()
    assert actual_rows == value_in_text, \
        f"Fact rows on page {actual_rows} does not matches with value on the top of table: {value_in_text}"


@pytest.mark.addition
def test_add_new_row_and_check(fixture_open_page, table='Categories', new_row=NEW_CATEGORY_DATA, expected=9):
    fixture_open_page.start_page.restore_data()
    fixture_open_page.start_page.execute_query(QueriesCustomers.ADD_NEW_ROW(table, new_row))
    fixture_open_page.start_page.wait_table_update()
    categories_amount = fixture_open_page.start_page.get_num_of_records(table)
    assert expected == categories_amount, f"Rows number does not matches with expected value (expected: {expected}," \
                                          f"found: {categories_amount}"
