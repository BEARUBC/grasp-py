import math

import numpy as np
import pandas as pd
from influxdb_client import InfluxDBClient, WriteOptions

from src.grasp_analytics.module import Module


class EMG(Module):
    # Two EMG channels, 0: bicep, 1: tricep
    num_channels = 2
    data = np.array([])

    def __init__(self, sensitivity=10):
        self.sensor_cache_length = 1000
        self.results_cache_length = 1000
        self.theta = [x / sensitivity for x in range(sensitivity, 0, -1)]
        self.data = np.zeros((self.num_channels, self.sensor_cache_length))
        self.results = []
        self.url = "http://localhost:8086"
        self.token = "Rbg3aKBu-nU_wY9wXkxCVLzT9WhH725mZ6LwEQgQjrppmeLYZ1J9xrjqXlZz6-oLfDJQhJWE169pyaN9rpmDzg=="
        self.org = "0ed254cf3dca2b2b"
        self.bucket = "GRASPDB"
        self.lag = 20
        self.peaks: list = [0] * self.lag
        self.threshold: float = 6000
        self.numthresholds = 4

    def run(self, input_json: dict) -> dict:
        new_data = input_json["emg_buffer"]

        out_contractions = []
        time = 0
        for data_point in new_data:
            time += 1
            curr_contraction = self.next_value(data_point)
            threshold_contraction = self.threshold_value(curr_contraction)
            out_contractions.append(threshold_contraction)
            self.influx_write(threshold_contraction, time)

        return {"contractions": out_contractions}

    def add_to_cache(self, val: np.array):
        self.data = np.concatenate(self.data, val, axis=0)
        self.data = self.data[-self.sensor_cache_length:, :]

    def apply_model_to_df(self, data_df):
        """Applies a model to the data and provides a moving average.

        Parameters
        ----------
        data_df : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        y_data = list(data_df)
        y = [0] * len(y_data)

        for j in range(len(self.theta), len(y)):
            for i in range(len(self.theta)):
                y[j] += self.theta[i] * y_data[j - i]

        pd_df = pd.DataFrame([(i, y[i]) for i in range(len(y))], columns=["x", "y"])
        pd_df["y"] = pd_df["y"].map(lambda x: ((1 / (1 + math.exp(-x))) - 0.5) * 2) #
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

    def threshold_value(self, val):
        if len(self.results) < self.lag:
            return 0

        self.peaks += [0]
        self.peaks.pop(0)

        for x in range(1, (self.numthresholds + 1)):
            new_threshold = self.threshold * (x / self.numthresholds)
            if val > new_threshold:
                self.peaks[-1] = x / self.numthresholds

        return self.peaks[-1]

    # Look into
    def influx_write(self, measurement, time):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as _client:
            # change write options params based on data batching
            # see https://github.com/influxdata/influxdb-client-python#writes
            with _client.write_api(
                write_options=WriteOptions(
                    batch_size=500,
                    flush_interval=10_000,
                    jitter_interval=2_000,
                    retry_interval=5_000,
                    max_retries=5,
                    max_retry_delay=30_000,
                    exponential_base=2,
                )
            ) as _write_client:

                _write_client.write(
                    self.bucket,
                    self.org,
                    {
                        "measurement": "emg contractions",
                        "tags": [],
                        "fields": {"contractions": measurement},
                        "time": time,
                    },
                )
