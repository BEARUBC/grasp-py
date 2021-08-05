import threading
import time
from typing import List

from src.data_generation.battery.battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processeslist: List[BatteryProcess], buffertime: float):
        self.processes = processeslist
        self.batterylife = 100
        self.buffertime = buffertime

    def reduce_battery(self):
        for process in self.processes:
            depletion = process.batteryusage
            is_turned_on = process.turnedon
            name = process.processname

            if is_turned_on:
                self.batterylife -= depletion
                print("Battery = " + str(self.batterylife) + " (" + name + " -" + str(depletion) + ")")

    # def add_process(self, newprocess: BatteryProcess, waittime=0.0):
    #     time.sleep(waittime)
    #     self.processes.append(newprocess)
    #
    #     print(newprocess.processname + " process added!")

    # def set_state(self, process: BatteryProcess, state: bool, waittime=0.0):
    #     time.sleep(waittime)
    #     process.turnedon = state
    #
    #     print("Set " + process.processname + " to " + state)

    def run_processes(self):
        # Start a timer that will do random iterations for changing the states
        if self.batterylife > 0:
            threading.Timer(self.buffertime, self.run_processes).start()
            self.reduce_battery()
        else:
            print("Battery Depleted")
