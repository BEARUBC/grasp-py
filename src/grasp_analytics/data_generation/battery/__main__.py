from battery_process import BatteryProcess
from export_simulation import export_results

num_simulations = 10
process_names = ["EMG", "Haptic", "GripSelect", "Other"]
process_mean_mean = 0.1
process_mean_range = 0.1
process_stdev_mean = 0.1
process_stdev_range = 0.1

export_results(num_simulations, process_names, process_mean_mean,
               process_mean_range, process_stdev_mean, process_stdev_range)
