import allure
import pytest

from utils.ui.helpers.application import Application

from conf import BASE_URL


@pytest.fixture(scope='session')
def fixture_open_page():
    with allure.step("Открытие браузера"):
        app = Application("chrome", BASE_URL)
    app.open_start_page()
    yield app
    app.destroy()
