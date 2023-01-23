import json
import os
from distutils.util import strtobool

config = None

LOCAL_START = strtobool(os.getenv('LOCAL_START', 'True'))
ENV = os.getenv('ENV', 'test')

if LOCAL_START:
    WEB_DRIVER_URL = 'http://localhost:4444/wd/hub'
else:
    WEB_DRIVER_URL = 'http://driver:4444/wd/hub'


def load_config(file):
    global config
    if config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            return json.load(f)
    return config


web_configs = load_config("config_test.json")[ENV]["web"]

BASE_URL = os.getenv('BASE_URL', web_configs["base_page"])
START_URL = os.getenv('START_URL', web_configs["start_page"])
