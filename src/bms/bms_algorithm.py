class BatteryAlgorithm:
    # Current implementation only works for one singular process that turns on/off at any time

    def __init__(self, process_mean: int = 0, current_battery: int = 100):
        self.process_mean = process_mean
        self.current_battery = current_battery

    def calculate_mean(self, battery_life: int):
        depletion = self.current_battery - battery_life

        if self.process_mean == 0:
            self.process_mean = depletion
        else:
            self.process_mean = (self.process_mean + depletion) / 2

        self.current_battery = battery_life
