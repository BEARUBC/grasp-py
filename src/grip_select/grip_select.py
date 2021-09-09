from enum import IntEnum

from src.grip_select.crop_cnn.crop_cnn import CropCNNSelector
from src.grip_select.mobilenet.analyzer import MobileNetAnalyzer
from src.grip_select.selector import GripSelector
from src.module import Module


class GripSelectModel(IntEnum):
    CROP_CNN = 0,
    MOBILENET = 1


class GripSelect(Module):
    def __init__(self, mode: GripSelectModel):
        self.mode = mode
        if self.mode == GripSelectModel.CROP_CNN:
            self._selector: GripSelector = CropCNNSelector()
        else:
            self._selector: GripSelector = MobileNetAnalyzer()

    def _process(self, input_json: dict) -> dict:
        pass
