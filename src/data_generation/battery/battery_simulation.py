import random
import time
from typing import List, Generator

from src.data_generation.battery.battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processes_list: List[BatteryProcess], buffertime: float):
        self.processes = processes_list
        self.battery_life = 100
        self.buffertime = buffertime

    def reduce_battery(self):
        for process in self.processes:
            depletion = process.batteryusage
            is_turned_on = process.turnedon
            name = process.processname

            if is_turned_on:
                if self.battery_life - depletion < 0 and self.battery_life > 0:
                    self.battery_life = 0
                    print("Battery = " + str(self.battery_life) + " (" + name + " -" + str(depletion) + ")")
                elif self.battery_life - depletion < 0 and self.battery_life <= 0:
                    self.battery_life = 0
                else:
                    self.battery_life -= depletion
                    print("Battery = " + str(self.battery_life) + " (" + name + " -" + str(depletion) + ")")

    def run_simulation(self, real_time: bool = False, change_frequency: float = 0.40) -> Generator[int, None, None]:
        rand_cutoff = 100 * change_frequency

        while self.battery_life > 0:
            yield self.battery_life
            self.reduce_battery()

            rand_number = random.randint(0, 100)
            if rand_number <= rand_cutoff:
                selected_index = random.randint(0, len(self.processes) - 1)
                selected_process = self.processes[selected_index]

                selected_process.turnedon = not selected_process.turnedon
                print("Set " + str(selected_process.processname) + " to " + str(selected_process.turnedon))

            if real_time:
                time.sleep(self.buffertime)

        yield self.battery_life
        print("Battery Depleted")
