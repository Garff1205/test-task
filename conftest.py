import allure
import pytest

from utils.ui.helpers.application import Application

from conf import BASE_URL


@pytest.fixture(scope='session')
def fixture_open_page():
    with allure.step("Open browser and go to the start page"):
        app = Application("chrome", BASE_URL)
    app.open_start_page()
    yield app
    app.destroy()
