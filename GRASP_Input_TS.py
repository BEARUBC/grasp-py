#!/usr/bin/python

from GRASP_Input import GRASP_Input
from guizero import App, Text, PushButton
from time import sleep

class GRASP_Input_TS(GRASP_Input):
    activated = True
    @staticmethod
    def reactivate():
        GRASP_Input_TS.activated = True
        pass

    def received_grip_callback(self, grip):
        if(GRASP_Input_TS.activated):
            self.grip_message.value = grip
            self.queue.put(grip)
        else:
            print("blocked")
    def setup(self):
        pass

    def run(self):
        print("start Ts")
        app = App(title="Hello world")
        self.grip_message = Text(app, text="No Grip Selected.")
        grip_1 = PushButton(app, command=self.received_grip_callback, args=["Cup"], text="Cup")
        app.display()

    @staticmethod
    def deactivate():
        GRASP_Input_TS.activated = False
        pass
