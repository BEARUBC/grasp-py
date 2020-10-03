import os

import yaml


def load_settings():
    with open(SETTINGS_PATH, "r") as settings_file:
        settings = yaml.load(settings_file, Loader=yaml.FullLoader)
    return settings


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(ROOT_DIR, '../settings.yaml')
SETTINGS = load_settings()
