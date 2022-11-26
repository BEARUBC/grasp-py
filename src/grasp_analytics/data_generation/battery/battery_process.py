class BatteryProcess:

    def __init__(self, process_name: str, mean_usage: float = 0, start_state: bool = False, usage_stdev: float = 0):
        self.process_name: str = process_name
        self.mean_usage: float = mean_usage
        self.usage_stdev: float = usage_stdev
        self.turned_on: bool = start_state
