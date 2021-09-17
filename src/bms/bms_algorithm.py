from typing import List

from src.data_generation.battery.battery_process import BatteryProcess


class BMSAlgorithm:
    def __init__(self, processes: List[BatteryProcess]):
        idle_process = BatteryProcess('idle', start_state=True)
        processes_list = [idle_process]

        self.processes = processes_list.append(processes)
        self.current_battery = 100
        self.buckets = {0: [0]}  # initialize dictionary with idle process first


    def bucket_values(self, battery_life: int):
        bucket_index = 0

        for process in self.processes:
            if process.turned_on:
                bucket_index += self.processes.index(process)

        depletion = self.current_battery - battery_life
        if bucket_index in self.buckets:
            self.buckets[bucket_index].append(depletion)
        else:
            self.buckets[bucket_index] = [depletion]

        self.current_battery = battery_life


    def calculate_means(self):
        # TODO: create an algorithm that determines each average based on a set of linear equations(?)

