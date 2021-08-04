class BatteryProcess:

    def __init__(self, processname: str, batteryusage: int):
        self.processname = processname
        self.batteryusage = batteryusage
        self.turnedon = True

    def set_process_state(self, state: str):
        # State can only be 'on' or 'off'
        if state == 'on':
            self.turnedon = True
        if state == 'off':
            self.turnedon = False
