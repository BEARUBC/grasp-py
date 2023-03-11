import os
from pathlib import Path

# import torch
import yaml


def load_settings():
    with open(SETTINGS_PATH, "r") as settings_file:
        settings = yaml.load(settings_file, Loader=yaml.FullLoader)
    return settings


SRC_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = Path(SRC_DIR)
SETTINGS_PATH = os.path.join(SRC_DIR, "../../settings.yaml")
SETTINGS = load_settings()
ROOT_PATH = (SRC_PATH / "../..").resolve()
DATA_PATH = (ROOT_PATH / "{0}".format(SETTINGS["emg"]["data_dir"])).resolve()
# TORCH_DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

INFLUX_URL = ""
INFLUX_TOKEN = ""
INFLUX_ORG = ""
