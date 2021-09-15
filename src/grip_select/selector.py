from abc import abstractmethod
from typing import List

import numpy as np
from sklearn.metrics import confusion_matrix

from src.grip_select.grip import GripType


class GripSelector:
    @abstractmethod
    def classify_image(self, image) -> GripType:
        pass

    def evaluate(self, images: List[np.ndarray], labels: List[GripType]) -> np.array:
        """
        (image, true_label) -> classifier -> (predicted_label, true_label) -> are predicted_label and true_label the same?
        """
        y_true = [int(x) for x in labels]
        image_classifications: List[GripType] = []
        # Cast classifications to ints
        predicted_grip_ints: list[int] = []
        return confusion_matrix(y_true, predicted_grip_ints)
