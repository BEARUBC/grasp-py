import numpy as np
from abc import abstractmethod, ABCMeta

from src.definitions import SETTINGS


class DataReader(metaclass=ABCMeta):
    def __init__(self):
        self.settings = SETTINGS["fsr_matrix"]
        self.reading_length = self.settings["dims"][0] * self.settings["dims"][1]
        self.available = True

    @abstractmethod
    def read_line(self):
        pass

    def get_frame(self, normalize=True):
        line = self.read_line()
        reading = np.reshape(line, tuple(self.settings["dims"]))

        if normalize:  # Normalize reading
            reading /= 1024.0
        return reading
