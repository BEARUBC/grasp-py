from typing import List

import cv2
import numpy as np
import torch
from sklearn.metrics import confusion_matrix

from src.definitions import TORCH_DEVICE
from src.grip_select.crop_cnn.grip_classifier import GripConvNet
from src.grip_select.crop_cnn.objectness import get_best_obj_img
from src.grip_select.grip import GripType
from src.grip_select.selector import GripSelector


class CropCNNSelector(GripSelector):

    def __init__(self, model: GripConvNet = None):
        self.model = model
        if self.model is None:
            self.model = GripConvNet().to(TORCH_DEVICE)

    @classmethod
    def load_model(cls, path):
        pass

    def classify_image(self, image: np.ndarray) -> GripType:
        # Normalize image to [-1, 1]
        desired_object_image = get_best_obj_img(image) / 128 - 1
        # Move channels to first axis
        rolled = np.moveaxis(desired_object_image, 2, 0).astype(np.float32)
        # Convert to batchable tensor
        im_tensor = torch.unsqueeze(torch.from_numpy(rolled).to(TORCH_DEVICE), 0)
        # Get model estimation
        grip = self.model(im_tensor).detach().numpy()
        # Convert model estimation to grip
        grip_type = GripType(np.argmax(grip[0]))
        return grip_type

    def evaluate(self, images: List[np.ndarray], labels: List[GripType]) -> confusion_matrix:
        """
        (image, true_label) -> classifier -> (predicted_label, true_label) -> are predicted_label and true_label the same?
        """
        y_true = [int(x) for x in labels]
        image_classifications: List[GripType] = []
        # Cast classifications to ints
        predicted_grip_ints: list[int] = []
        return confusion_matrix(y_true, predicted_grip_ints)
