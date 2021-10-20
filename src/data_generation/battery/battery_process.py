class BatteryProcess:

    def __init__(self, process_name: str, battery_usage: float = 0, start_state: bool = False):
        self.process_name: str = process_name
        self.battery_usage: float = battery_usage
        self.turned_on: bool = start_state
