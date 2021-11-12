from src.module import Module
from src.bms.bms_algorithm import BMSAlgorithm


class BMS(Module):

    def __init__(self, input_json: dict):
        self.bms_solver = BMSAlgorithm()
        self.battery_life: float = input_json["current_battery"]
        self.processes: list = input_json["processes_list"]

        self.bms_solver.set_battery(self.battery_life)
        self.bms_solver.set_processes(self.processes)

    def _process(self, input_json: dict) -> dict:
        current_battery = input_json["current_battery"]
        self.bms_solver.create_datapoint(current_battery)

        process_usages = self.bms_solver.get_process_usages()
        return {"bms_process_usages": process_usages}
