import random as rand

from src.data_generation.battery.battery_process import BatteryProcess
from src.data_generation.battery.battery_simulation import BatterySimulation
from src.bms.bms_algorithm import BMSAlgorithm

rand_means = []
for i in range(4):
    n = rand.uniform(0.2, 1)
    rand_means.append(n)

rand_noise = []
for i in range(4):
    n = rand.uniform(0.01, 0.2)
    rand_noise.append(n)

emg_process = BatteryProcess('EMG', mean_usage=rand_means[0], start_state=False, noise=rand_noise[0])
hapticfeedback_process = BatteryProcess('Haptic_Feedback', mean_usage=rand_means[1], start_state=False, noise=rand_noise[1])
camera_process = BatteryProcess('Camera', mean_usage=rand_means[2], start_state=False, noise=rand_noise[2])
camera_3d_process = BatteryProcess('Camera3D', mean_usage=rand_means[3], start_state=False, noise=rand_noise[3])

process_list = [emg_process, hapticfeedback_process, camera_process, camera_3d_process]
sleep_time = 5

bms_solver = BMSAlgorithm(process_list)
battery_simulation = BatterySimulation(process_list, sleep_time)
for battery_life in battery_simulation.run_simulation():
    bms_solver.create_datapoint(battery_life)

print(bms_solver.get_process_usages())
print(rand_means)
print(rand_noise)

# To-do
# Create noise per process and in the battery simulation to create variability in data
# Numpy normal distribution using gaussian