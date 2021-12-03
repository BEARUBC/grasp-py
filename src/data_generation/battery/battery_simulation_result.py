from dataclasses import dataclass
from typing import List


@dataclass
class BatterySimulationResult:
    process_states: List[List[bool]]
    battery_reductions: List[float]
    battery_overall: List[float]