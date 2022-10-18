import random
import time
import pandas as pd
from typing import List

from battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processeslist: List[BatteryProcess], buffertime: float, create_csv: bool):
        self.processes = processeslist
        self.batterylife = 100
        self.buffertime = buffertime
        self.create_csv = create_csv
        if self.create_csv:
            self.csv_data = []

    def reduce_battery(self):
        for process in self.processes:
            depletion = process.batteryusage
            is_turned_on = process.turnedon
            name = process.processname

            if is_turned_on:
                if self.batterylife - depletion < 0 and self.batterylife > 0:
                    self.batterylife = 0
                    print(
                        "Battery = "
                        + str(self.batterylife)
                        + " ("
                        + name
                        + " -"
                        + str(depletion)
                        + ")"
                    )
                elif self.batterylife - depletion < 0 and self.batterylife <= 0:
                    self.batterylife = 0
                else:
                    self.batterylife -= depletion
                    print(
                        "Battery = "
                        + str(self.batterylife)
                        + " ("
                        + name
                        + " -"
                        + str(depletion)
                        + ")"
                    )

                if self.create_csv:
                    data = [0] * (len(self.processes) + 1)
                    index = self.processes.index(process)
                    data[0] = self.batterylife

                    if self.batterylife == 0:
                        data[index + 1] = self.csv_data[len(self.csv_data)-1][0]
                    else:
                        data[index + 1] = depletion

                    self.csv_data.append(data)

    def run_simulation(self, change_frequency: float = 0.40):
        rand_cutoff = 100 * change_frequency

        while self.batterylife > 0:
            self.reduce_battery()

            rand_number = random.randint(0, 100)
            if rand_number <= rand_cutoff:
                selected_index = random.randint(0, len(self.processes) - 1)
                selected_process = self.processes[selected_index]

                if selected_process.turnedon:
                    selected_process.turnedon = False
                else:
                    selected_process.turnedon = True
                print(
                    "Set "
                    + str(selected_process.processname)
                    + " to "
                    + str(selected_process.turnedon)
                )

            time.sleep(self.buffertime)

        print("Battery Depleted")

        if self.create_csv:
            cols = ["Battery"]
            for process in self.processes:
                cols.append(process.processname)
            df = pd.DataFrame(self.csv_data, columns=cols)
            df.to_csv('csv_outputs/output.csv', index=False)
