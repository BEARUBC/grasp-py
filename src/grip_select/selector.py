from abc import abstractmethod


class GripSelector:
    @abstractmethod
    def classify_image(self, image):
        pass
