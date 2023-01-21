import json
import os

config = None

DOCKER_WEB_DRIVER = 'http://driver:4444/wd/hub'
ENV = os.getenv('ENV', 'test')


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
