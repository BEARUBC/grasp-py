from abc import abstractmethod, ABCMeta

from definitions import SETTINGS


class DataReader(metaclass=ABCMeta):
    def __init__(self):
        self.settings = SETTINGS["fsr_matrix"]

    def parse_line(self):
        return self.parse_reading(self.read_line())

    @abstractmethod
    def read_line(self):
        pass

    # Convert matrix data to network inputs
    def parse_reading(self, line):
        # Number of cells in matrix
        reading_length = self.settings["rows"] * self.settings["columns"]
