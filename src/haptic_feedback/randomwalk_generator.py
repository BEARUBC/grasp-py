import matplotlib.pyplot as plt
import numpy as np

from src.definitions import SETTINGS


class RandomWalkGenerator:
    def __init__(self):
        self.settings = SETTINGS["haptic_feedback"]["randomwalk_generator"]
        self.plotsize = self.settings["default_plotsize"]
        self.datapoints = self.settings["default_numdatapoints"]
        self.randomwalk = []

    def generator(self):
        datapoints = self.datapoints

        steps = np.random.standard_normal(datapoints)
        steps[0] = 0
        self.randomwalk = np.cumsum(steps)

    def plotter(self):
        plot_size = self.plotsize
        rw = self.randomwalk

        plt.figure(figsize=plot_size)
        plt.plot(rw)
        plt.title("Simulated Random Walk")
        plt.show()
