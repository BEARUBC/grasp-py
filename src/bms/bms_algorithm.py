from typing import List

import numpy as np

from src.data_generation.battery.battery_process import BatteryProcess
from sklearn.linear_model import LinearRegression


class BMSAlgorithm:
    def __init__(self, processes: List[BatteryProcess], battery_life: float):
        self.processes = processes
        self.current_battery: float = battery_life
        self.model = LinearRegression()
        self.features = []
        self.labels = []

    def create_datapoint(self, battery_life: int):
        depletion = self.current_battery - battery_life
        self.features.append([int(x.turned_on) for x in self.processes])
        self.labels.append(depletion)
        self.current_battery = battery_life

    def get_process_usages(self):
        x = np.array(self.features)
        y = np.array(self.labels)
        self.model.fit(x, y)
        return [*self.model.coef_, self.model.intercept_]

