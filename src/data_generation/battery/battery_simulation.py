import random
import time
import numpy as np
from typing import List, Generator

from influxdb_client import InfluxDBClient, WriteOptions
from datetime import datetime
from src.data_generation.battery.battery_process import BatteryProcess


class BatterySimulation:
    def __init__(self, processes_list: List[BatteryProcess], buffertime: float = 0):
        self.processes = processes_list
        self.battery_life: float = 100
        self.buffertime = buffertime
        self.num_processes = len(self.processes)
        # for influx:
        self.url = "http://localhost:8086"
        self.token = "Rbg3aKBu-nU_wY9wXkxCVLzT9WhH725mZ6LwEQgQjrppmeLYZ1J9xrjqXlZz6-oLfDJQhJWE169pyaN9rpmDzg=="
        self.org = "0ed254cf3dca2b2b"
        self.bucket = "GRASPDB"

    def reduce_battery(self):
        for process in self.processes:
            mu = process.mean_usage
            sigma = process.usage_stdev
            is_turned_on = process.turned_on

            depletion = abs(np.random.normal(mu, sigma))

            if is_turned_on:
                if self.battery_life - depletion < 0 and self.battery_life > 0:
                    process.mean_usage = self.battery_life
                    self.battery_life = 0
                    # print("Battery = " + str(self.battery_life) + " (" + name + " -" + str(depletion) + ")")
                elif self.battery_life - depletion < 0 and self.battery_life <= 0:
                    process.mean_usage = 0
                    self.battery_life = 0
                else:
                    self.battery_life -= depletion
                    # print("Battery = " + str(self.battery_life) + " (" + name + " -" + str(depletion) + ")")
                # self.influx_write(self.battery_life, datetime.now(), name)

    def run_simulation(self, change_frequency: float = 0.40) -> Generator[int, None, None]:
        rand_cutoff = 100 * change_frequency


        while self.battery_life > 0:
            self.reduce_battery()
            yield self.battery_life

            rand_number = random.randint(0, 100)
            if rand_number <= rand_cutoff:
                selected_index = random.randint(0, len(self.processes) - 1)
                selected_process = self.processes[selected_index]

                selected_process.turned_on = not selected_process.turned_on
                # print("Set " + str(selected_process.process_name) + " to " + str(selected_process.turned_on))

            if self.buffertime > 0:
                time.sleep(self.buffertime)
        yield 0
        print("Battery Depleted")

    def create_tuples(self, simulation_list: List[int]) -> List:
        num = self.num_processes + 1
        return list(zip(*[iter(simulation_list)]*num))


    def influx_write(self, measurement, current_time, tag):
        with InfluxDBClient(url=self.url, token=self.token, org=self.org) as _client:
            # change write options params based on data batching
            # see https://github.com/influxdata/influxdb-client-python#writes
            with _client.write_api(write_options=WriteOptions(batch_size=500, flush_interval=10_000,
                                                              jitter_interval=2_000, retry_interval=5_000,
                                                              max_retries=5, max_retry_delay=30_000,
                                                              exponential_base=2)) as _write_client:

                _write_client.write(self.bucket, self.org,
                                    {"measurement": "current battery level", "tags": {"current process": tag},
                                     "fields": {"battery": measurement}, "time": current_time})