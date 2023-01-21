from selenium.webdriver.common.by import By


class LocatorStart(object):
    RUN_BUTTON = By.CLASS_NAME, 'ws-btn'
    # используем немного не красивую конструкцию [id=...] вместо #... так как DevTools браузера по запросу #divResultSQL
    # находит кроме элемента с указанным айдишником еще и стиль с именем #divResultSQL, не уверен что WebDriver не
    # сделает так же, поэтому перестрахуемся пожертвовав изящностью кода.
    RESULT_TABLE = By.CSS_SELECTOR, '[id="divResultSQL"] table'
    NUMBER_OF_RECORDS = By.CSS_SELECTOR, '[id="divResultSQL"] div[style*="margin-bottom:"]'
    TABLE_UPDATE_MESSAGE = By.XPATH, "//*[@id='divResultSQL']//div[contains(text(),'You have made changes to " \
                                     "the database.')]"


class LocatorCodeMirror(object):
    CODE_MIRROR = By.CLASS_NAME, 'CodeMirror'
    LINE = By.CLASS_NAME, 'CodeMirror-line'
    TEXT_AREA = By.CSS_SELECTOR, 'textarea'
