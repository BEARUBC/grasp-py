#!/usr/bin/python

from GRASP_Input import GRASP_Input
from time import sleep

class GRASP_Input_Voice(GRASP_Input):

    @staticmethod
    def reactivate():
        pass

    def received_grip_callback(self, grip):
        self.queue.put(grip)

    def setup(self):
        pass

    def run(self):
        print("start Voice")
        while(True):
            self.received_grip_callback("ball")
            sleep(15)

    @staticmethod
    def deactivate():
        pass
