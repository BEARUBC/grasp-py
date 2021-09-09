from abc import abstractmethod

from src.grip_select.grip import GripType


class GripSelector:
    @abstractmethod
    def classify_image(self, image) -> GripType:
        pass
