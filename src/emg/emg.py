from abc import ABC

import numpy as np
from scipy import ndimage

from src.module import Module


class EMG (Module):
    channels = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])  # each row contains channels corresponding to a muscle group
    num_channels = channels[:].size
    window_size = -1
    num_windows = -1
    data = np.array([])

    MEDFILT_KERNEL = 11  # size of filter kernel
    VOLT_THRESH = 128  # threshold for peak detection; this method might not work
    SAMPLE_THRESH = 20  # number of samples above voltage threshold needed to count as a peak
    VOTE_THRESH = 2  # number of channel votes needed to count as a peak

    def __init__(self, window_size, num_windows):
        self.window_size = window_size  # number of samples to read for each channel (sample time * sample rate)
        self.num_windows = num_windows  # number of past windows to keep
        self.data = np.zeros((self.num_channels, self.window_size * self.num_windows))

    def process(self, input_json: dict) -> dict:
        self.data = np.roll(input_json, -self.window_size, axis=1)
        for c in self.channels[:]:
            self.data[c, -self.window_size:] = input_json[c]
        return {"data": self.data}

    def thresh_peak(self, signal):  # detect peak based on threshold
        if (signal[signal >= self.VOLT_THRESH].size >= self.SAMPLE_THRESH):
            return True
        else:
            return False

    def peak_detect(self):  # detects peaks for muscle groups
        # Pre-processing
        # TODO: envelope detection
        cleaned = ndimage.median_filter(self.data, (1, self.MEDFILT_KERNEL))  # median filter to remove outliers
        # Peak detection
        print(self.channels.shape)
        peak = np.zeros(self.channels.shape[0])
        for i in range(0, peak.size):
            for j in range(0, self.channels[i].size):
                peak[i] += self.thresh_peak(cleaned[self.channels[i, j], :])
        return peak >= self.VOTE_THRESH
