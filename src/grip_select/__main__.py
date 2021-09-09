import cv2
import torch

from src.definitions import ROOT_PATH, SETTINGS, TORCH_DEVICE
from src.grip_select.grip_select import GripSelect, GripSelectModel

img_path = ROOT_PATH / SETTINGS["grip_select"]["data_dir"] / "images/cup/cup_001.jpg"
im = cv2.imread(str(img_path))
grip_select = GripSelect(GripSelectModel.CROP_CNN)
classification = grip_select._selector.classify_image(im)
