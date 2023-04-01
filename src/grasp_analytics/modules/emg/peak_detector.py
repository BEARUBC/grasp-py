import numpy as np

from src.grasp_analytics.definitions import SETTINGS


class PeakDetector:
    def __init__(
        self, lag: int, threshold: float, influence: float, numthresholds: int
    ):
        self.settings = SETTINGS["emg"]["peak_detection"]
        self.lag: int = lag # number of signals at the beginning to ignore
        self.threshold: float = threshold
        self.influence: float = influence # between 0 and 1
        self.y: list = [0] * self.lag  # raw signals
        self.signals: list = [0] * self.lag # peaks
        self.filteredY = [0] * self.lag # filtered with influence of previous signals
        self.avgFilter: list = [0] * self.lag # average of filtered signals
        self.stdFilter: list = [0] * self.lag # std of filtered signals
        self.avgFilter[self.lag - 1] = self.settings["default_mean"]
        self.stdFilter[self.lag - 1] = self.settings["default_std"]
        self.data_points_seen = 0 # number of points already thresholded
        self.numthresholds = numthresholds

    def threshold_new_val(self, new_value):
        self.data_points_seen += 1
        self.y.append(new_value)
        self.y.pop(0)
        if self.data_points_seen < self.lag:
            return 0

        self.signals += [0]
        self.signals.pop(0)
        self.filteredY += [0]
        self.filteredY.pop(0)
        self.avgFilter += [0]
        self.avgFilter.pop(0)
        self.stdFilter += [0]
        self.stdFilter.pop(0)

        self.filteredY[-1] = (
                self.influence * self.y[-1]
                + (1 - self.influence) * self.filteredY[-2]
        )  # takes into account previous signal
        self.avgFilter[-1] = np.mean(self.filteredY[:-1])  # new average
        self.stdFilter[-1] = np.std(self.filteredY[:-1])  # new std

        x = 1
        while x <= self.numthresholds: # loop through all thresholds
            newthreshold = self.threshold * (x / self.numthresholds) # multiple thresholds are fractions of largest threshold
            # if abs(self.y[-1] - self.avgFilter[-2]) > (newthreshold * self.stdFilter[-2]):
            if self.y[-1] > newthreshold: # passes current threshold
                self.signals[-1] = x / self.numthresholds # signal is normalized threshold
            x = x + 1

        return self.signals[-1]
