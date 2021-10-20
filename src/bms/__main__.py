from src.data_generation.battery.battery_process import BatteryProcess
from src.data_generation.battery.battery_simulation import BatterySimulation
from src.bms.bms_algorithm import BMSAlgorithm

emg_process = BatteryProcess('EMG', 0.1, start_state=False)
hapticfeedback_process = BatteryProcess('Haptic_Feedback', 0.05, start_state=False)
camera_process = BatteryProcess('Camera', 0.13, start_state=False)
camera_3d_process = BatteryProcess('Camera3D', 0.3, start_state=False)

process_list = [emg_process, hapticfeedback_process, camera_process, camera_3d_process]
sleep_time = 5

bms_solver = BMSAlgorithm(process_list)
battery_simulation = BatterySimulation(process_list, sleep_time)
for battery_life in battery_simulation.run_simulation():
    bms_solver.create_datapoint(battery_life)

print(bms_solver.get_process_usages())

# To-do
# Create noise per process and in the battery simulation to create variability in data
# Numpy normal distribution using gaussian