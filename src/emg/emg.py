import math

import numpy as np
import pandas as pd

from src.module import Module


class EMG (Module):
    # Two EMG channels, 0: bicep, 1: tricep
    num_channels = 2
    data = np.array([])


    def __init__(self, sensitivity=10):
        self.sensor_cache_length = 1000
        self.results_cache_length = 1000
        self.theta = [x / sensitivity for x in range(sensitivity, 0, -1)]
        self.data = np.zeros((self.num_channels, self.sensor_cache_length))
        self.results = []

    def _process(self, input_json: dict) -> dict:
        new_data = input_json["emg_buffer"]

        out_contractions = []
        for data_point in new_data:
            out_contractions.append(self.next_value(data_point))

        # TODO: push new data to influx

        return {"contractions": out_contractions}

    def add_to_cache(self, val: np.array):
        self.data = np.concatenate(self.data, val, axis=0)
        self.data = self.data[-self.sensor_cache_length:, :]

    def apply_model_to_df(self, data_df):
        y_data = list(data_df)
        y = [0] * len(y_data)

        for j in range(len(self.theta), len(y)):
            for i in range(len(self.theta)):
                y[j] += self.theta[i] * y_data[j - i]

        pd_df = pd.DataFrame([(i, y[i]) for i in range(len(y))], columns=["x", "y"])
        pd_df["y"] = pd_df["y"].map(lambda x: ((1 / (1 + math.exp(-x))) - 0.5) * 2)
        return pd_df

    def next_value(self, val: np.array):
        self.add_to_cache(val)
        y = 0
        for i in range(len(self.theta)):
            data_idx = -len(self.theta) + i
            # Bicep - tricep to get desired contraction level.
            data_point_diff = self.data[data_idx, 0] - self.data[data_idx, 1]
            y += self.theta[-i - 1] * data_point_diff

        y /= sum(self.theta)

        self.results.append(y)
        return y
