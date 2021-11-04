class BatteryProcess:

    def __init__(self, process_name: str, mean_usage: float = 0, start_state: bool = False, noise: float = 0):
        self.process_name: str = process_name
        self.mean_usage: float = mean_usage
        self.noise: float = noise
        self.turned_on: bool = start_state
