import random

from src.data_generation.battery.battery_process import BatteryProcess
from src.data_generation.battery.battery_simulation import BatterySimulation


def main():
    emg_process = BatteryProcess('EMG', 5, startstate=True)
    hapticfeedback_process = BatteryProcess('Haptic_Feedback', 5, startstate=True)
    camera_process = BatteryProcess('Camera', 3, startstate=True)
    test_process = BatteryProcess('Test', 10)

    process_list = [emg_process, hapticfeedback_process, camera_process]
    sleep_time = 5
    # random_time = random.randint(1, 20)
    # random_time2 = random.randint(1, 20)

    battery_simulation = BatterySimulation(process_list, sleep_time)
    battery_simulation.run_processes()

    # battery_simulation.set_state(test_process, True, random_time)
    # battery_simulation.set_state(camera_process, False, random_time2)


main()
