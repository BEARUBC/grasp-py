from src.data_generation.battery.battery_process import BatteryProcess
from src.data_generation.battery.battery_simulation import BatterySimulation
from src.bms.bms_algorithm import BMSAlgorithm

emg_process = BatteryProcess('EMG', 5, start_state=True)
hapticfeedback_process = BatteryProcess('Haptic_Feedback', 5, start_state=True)
camera_process = BatteryProcess('Camera', 3, start_state=True)
test_process = BatteryProcess('Test', 10)

process_list = [emg_process, hapticfeedback_process, camera_process, test_process]
sleep_time = 5

bms_solver = BMSAlgorithm(process_list)
battery_simulation = BatterySimulation(process_list, sleep_time)
battery_lives = battery_simulation.run_simulation()

for battery_life, activity in battery_simulation.run_simulation():
    bms_solver.create_datapoint(battery_life)
    print(battery_simulation.activity_tuple, bms_solver.buckets)
