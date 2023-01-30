import allure
from selenium import webdriver

from conf import WEB_DRIVER_URL, START_URL
from utils.ui.helpers.base import BaseHelper
from utils.ui.pages.start_page import StartPage


class Application:

    def __init__(self, browser: str, base_url: str):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-extensions')
            options.add_argument('--start-maximized')
            options.add_argument('--no-sandbox')
            options.add_argument('--enable-features=NetworkService')

            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors-spki-list')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-urlfetcher-cert-requests')
            options.add_argument('--disable-test-root-certs')
            options.add_argument('--allow-insecure-localhost')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--reduce-security-for-testing')

            self.wd = webdriver.Remote(command_executor=WEB_DRIVER_URL, options=options)

        self.base = BaseHelper(self)
        self.start_page = StartPage(self)

        self.base_url = base_url

    @allure.step("To the start page")
    def open_start_page(self):
        self.wd.get(self.base_url + START_URL)

    @allure.step('Session ending')
    def destroy(self):
        self.wd.quit()
