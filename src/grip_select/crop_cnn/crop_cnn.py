import cv2
import numpy as np

from src.grip_select.crop_cnn.grip_classifier import GripConvNet
from src.grip_select.crop_cnn.objectness import get_best_obj_img
from src.grip_select.grip import GripType
from src.grip_select.selector import GripSelector


class CropCNNSelector(GripSelector):

    def __init__(self, model: GripConvNet = None):
        self.model = model
        if self.model is None:
            self.model = GripConvNet()

    @classmethod
    def load_model(cls, path):
        pass

    def classify_image(self, image) -> GripType:
        desired_object_image = get_best_obj_img(image)
        grip = self.model(desired_object_image)
        return GripType(np.argmax(grip[0]))
