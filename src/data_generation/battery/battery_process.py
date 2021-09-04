class BatteryProcess:

    def __init__(self, process_name: str, battery_usage: int, start_state: bool = False):
        self.process_name: str = process_name
        self.battery_usage: int = battery_usage
        self.turned_on: bool = start_state
