"""
[Load Data] ->    }  [Evaluate model on data] -> [Get evaluation Results]
[Create Model] -> }
"""

import pandas as pd

from src.definitions import ROOT_PATH, SETTINGS
from src.grip_select.crop_cnn.crop_cnn import CropCNNSelector

data_path = ROOT_PATH / SETTINGS["grip_select"]["data_dir"] / "parsed/evaluate.csv"

data = pd.read_csv(str(data_path))
labels = pd[""]

selector = CropCNNSelector()
# selector_evaluation = selector.evaluate(data)