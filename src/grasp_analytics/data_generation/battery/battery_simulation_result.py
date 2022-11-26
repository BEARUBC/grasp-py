from dataclasses import dataclass
from typing import List


@dataclass
class BatterySimulationResult:
    """
    Dataclass that saves all relevant information for a given bms simulation

    process_states: a list of lists containing bool values whether each process is turned on
                    (each list in the main list should be of length = number of processes)
    battery_reductions: a list of floats identifying how much the battery got reduced at each time step
    battery_overall: a list of floats identifying how much battery remained at each time step
    """
    process_states: List[List[bool]]
    battery_reductions: List[float]
    battery_overall: List[float]
