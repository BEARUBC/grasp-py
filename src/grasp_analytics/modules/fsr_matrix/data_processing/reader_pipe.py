import sys
import json
from typing import Optional

import numpy as np

from src.grasp_analytics.definitions import SETTINGS
from .reader import DataReader


class PipeReader(DataReader):
    def __init__(self, port=None):
        super().__init__()
        self.settings.update(SETTINGS["communication"]["UART"])
        self.input = sys.stdin

    def get_frame(self, raw=False) -> Optional[np.ndarray]:
        # line = self.input.readline()
        # line = json.loads(sys.stdin.readline())
        line = [[0.0,0.0,0.0,0.0,0.0,0.0,0.0],[10.0,10.0,10.0,10.0,10.0,10.0,10.0],[9.0,9.0,9.0,9.0,9.0,9.0,9.0],[8.0,8.0,8.0,8.0,8.0,8.0,8.0],[7.0,7.0,7.0,7.0,7.0,7.0,7.0],[6.0,6.0,6.0,6.0,6.0,6.0,6.0],[5.0,5.0,5.0,5.0,5.0,5.0,5.0],[4.0,4.0,4.0,4.0,4.0,4.0,4.0],[3.0,3.0,3.0,3.0,3.0,3.0,3.0],[2.0,2.0,2.0,2.0,2.0,2.0,2.0],[1.0,1.0,1.0,1.0,1.0,1.0,1.0]]

        # line = [[2,2,2,2,2,2,2],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0],[10,10,10,10,10,10,10],[9,9,9,9,9,9,9],[8,8,8,8,8,8,8],[7,7,7,7,7,7,7],[6,6,6,6,6,6,6],[5,5,5,5,5,5,5],[4,4,4,4,4,4,4],[3,3,3,3,3,3,3]]

        reading = np.reshape(line, tuple(self.settings["dims"]))

        if not raw:  # Normalize reading
            reading = reading / self.settings["resolution"]
        return reading
