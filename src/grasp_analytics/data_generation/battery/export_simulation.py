import pickle
import numpy as np

from battery_process import BatteryProcess
from battery_simulation import BatterySimulation
from battery_simulation_result import BatterySimulationResult

"""
Run a bunch of simulations, and export the parameters and results of each one.
"""


def export_results(num_sims, names, mean_value, mean_range, stdev_value, stdev_range):
    sim_results = []
    for _ in range(num_sims):
        mean_usages = np.random.rand(len(names))
        mean_usages *= mean_range
        # Our distribution is now [0, process_mean_range]
        mean_usages += mean_value / 2
        # Our distribution is now [process_mean_mean / 2, process_mean_range + process_mean_mean / 2]

        usage_stdev = np.random.rand(len(names))
        usage_stdev *= stdev_range
        usage_stdev += stdev_value / 2

        processes = [
            BatteryProcess(
                names[i],
                mean_usages[i],
                usage_stdev=usage_stdev[i],
                start_state=False
            ) for i in range(len(names))
        ]

        battery_simulation = BatterySimulation(processes)
        process_states = []
        battery_reductions = []
        battery_overall = []
        last_battery = battery_simulation.battery_life
        for timestep in battery_simulation.run_simulation():
            process_states.append([x.turned_on for x in battery_simulation.processes])
            battery_reduction = battery_simulation.battery_life - last_battery
            battery_reductions.append(battery_reduction)
            last_battery = battery_simulation.battery_life
            battery_overall.append(last_battery)
        sim_result = BatterySimulationResult(process_states, battery_reductions, battery_overall)
        sim_results.append(sim_result)

    with open("battery_simulation_export.pkl", "wb") as f:
        pickle.dump(sim_results, f)
