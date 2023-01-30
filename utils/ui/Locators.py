from selenium.webdriver.common.by import By


class LocatorStart(object):
    RUN_BUTTON = By.CLASS_NAME, 'ws-btn'
    RESTORE_BUTTON = By.ID, 'restoreDBBtn'
    # We use not so beautiful construction [id=...] instead of #... because such search find styles to.
    RESULT_TABLE = By.CSS_SELECTOR, '[id="divResultSQL"] table'
    YOUR_DB_TABLE = By.CSS_SELECTOR, '[id="yourDB"] table'
    NUMBER_OF_RECORDS = By.CSS_SELECTOR, '[id="divResultSQL"] div[style*="margin-bottom:"]'
    TABLE_UPDATE_MESSAGE = By.XPATH, "//*[@id='divResultSQL']//div[contains(text(),'You have made changes to " \
                                     "the database.')]"


class LocatorCodeMirror(object):
    CODE_MIRROR = By.CLASS_NAME, 'CodeMirror'
    LINE = By.CLASS_NAME, 'CodeMirror-line'
    TEXT_AREA = By.CSS_SELECTOR, 'textarea'
