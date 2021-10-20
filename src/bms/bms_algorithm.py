from typing import List

from src.data_generation.battery.battery_process import BatteryProcess


class BMSAlgorithm:
    def __init__(self, processes: List[BatteryProcess]):
        idle_process = BatteryProcess('idle', start_state=True)
        processes_list = [idle_process]

        self.processes = processes_list.append(processes)
        self.current_battery = 100
        self.datapoints = []


    def create_datapoint(self, battery_life: int):
        depletion = self.current_battery - battery_life
        features = [int(x.turned_on) for x in self.processes] + [depletion]
        self.datapoints.append(tuple(features))
        self.current_battery = battery_life


    def calculate_means(self):
        # TODO: create an algorithm that determines each average based on a set of linear equations(?)


