import pandas as pd
from src.emg.parser import EMGParser
import math


class ContinuousEMGModel:
    def __init__(self, sensitivity=10):
        self.theta = [x / sensitivity for x in range(sensitivity, 0, -1)]
        self.cache_size = len(self.theta)
        self.cache = []
        self.results = []

    def add_to_cache(self, val):
        self.cache.append(val)
        if len(self.cache) >= self.cache_size:
            self.cache.pop(0)

    def apply_model_to_df(self, data_df, electrode_col="electrode_1"):
        y_data = list(data_df[electrode_col])
        y = [0] * len(y_data)

        for j in range(len(self.theta), len(y)):
            for i in range(len(self.theta)):
                y[j] += self.theta[i] * y_data[j - i]

        pd_df = pd.DataFrame([(i, y[i]) for i in range(len(y))], columns=["x", "y"])
        pd_df["y"] = pd_df["y"].map(lambda x: ((1 / (1 + math.exp(-x))) - 0.5) * 2)
        return pd_df

    def next_value(self, val):
        self.add_to_cache(val)
        y = 0
        for i in range(len(self.cache)):
            y += self.theta[i] * self.cache[len(self.cache) - i - 1]

        y /= sum(self.theta)

        self.results.append(y)
        return y