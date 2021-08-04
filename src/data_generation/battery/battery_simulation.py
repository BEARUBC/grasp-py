import threading
import time

from src.data_generation.battery.battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processeslist: list, buffertime: float):
        self.processes = processeslist
        self.batterylife = 100
        self.buffertime = buffertime

    def reduce_battery(self):
        for process in self.processes:
            depletion = getattr(process, 'batteryusage')
            is_turned_on = getattr(process, 'turnedon')
            name = getattr(process, 'processname')

            if is_turned_on:
                self.batterylife -= depletion
                print("Battery = " + str(self.batterylife) + " (" + name + " -" + str(depletion) + ")")

    def add_process(self, newprocess: BatteryProcess, waittime=0.0):
        time.sleep(waittime)
        self.processes.append(newprocess)

        print(newprocess.processname + " process added!")

    def set_state(self, process: BatteryProcess, state: str, waittime=0.0):
        time.sleep(waittime)
        set_process = process
        set_process.set_process_state(state)

        self.processes.remove(process)
        self.processes.append(set_process)

        print("Set " + set_process.processname + " to " + state)

    def run_processes(self):
        if self.batterylife > 0:
            threading.Timer(self.buffertime, self.run_processes).start()
            self.reduce_battery()
        else:
            print("Battery Depleted")
