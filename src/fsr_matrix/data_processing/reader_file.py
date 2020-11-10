from pathlib import Path

from src.fsr_matrix.data_processing.reader import DataReader


class FileReader(DataReader):
    def __init__(self, file_path: Path):
        super().__init__()
        self.file = open(file_path, "r")

    def read_line(self):
        line = self.file.readline()
        if not line:
            self.available = False
            self.file.close()
        return line

