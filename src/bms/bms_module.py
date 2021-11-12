from src.module import Module
from src.bms.bms_algorithm import BMSAlgorithm


class BMS(Module):

    def __init__(self, input_json: dict):
        self.bms_solver = BMSAlgorithm(input_json["processes_list"], input_json["current_battery"])

    def _process(self, input_json: dict) -> dict:
        current_battery = input_json["current_battery"]
        self.bms_solver.create_datapoint(current_battery)

        process_usages = self.bms_solver.get_process_usages()
        return {"bms_process_usages": process_usages}
