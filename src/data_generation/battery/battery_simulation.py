from src.data_generation.battery.battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processeslist: list):
        self.processes = processeslist
        self.batterylife = 100
        self.batteryisdepleted = False

    def reduce_battery(self):
        for process in self.processes:
            depletion = getattr(process, 'batteryusage')
            is_turned_on = getattr(process, 'turnedon')

            if is_turned_on:
                self.batterylife -= depletion

    def add_process(self, newprocess: BatteryProcess):
        self.processes.append(newprocess)
