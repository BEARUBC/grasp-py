from src.data_generation.battery.battery_process import BatteryProcess
from src.data_generation.battery.battery_simulation import BatterySimulation


emg_process = BatteryProcess('EMG', 5, start_state=True)
hapticfeedback_process = BatteryProcess('Haptic_Feedback', 5, start_state=True)
camera_process = BatteryProcess('Camera', 3, start_state=True)
test_process = BatteryProcess('Test', 10)

process_list = [emg_process, hapticfeedback_process, camera_process, test_process]
sleep_time = 5

battery_simulation = BatterySimulation(process_list, sleep_time)
battery_lives = list(battery_simulation.run_simulation())
test_tuple = battery_simulation.create_tuples(battery_lives)
print(test_tuple)
