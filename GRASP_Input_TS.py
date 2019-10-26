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
        try:
            print("start Ts")
            app = App(title="Hello world")
            self.grip_message = Text(app, text="No Grip Selected.")
            grip_0 = PushButton(app, command=self.received_grip_callback, args=["SAFETY_OFF"], text="SAFETY_OFF")
            grip_1 = PushButton(app, command=self.received_grip_callback, args=["Cup"], text="Cup")
            grip_2 = PushButton(app, command=self.received_grip_callback, args=["Hammer"], text="Hammer")
            grip_3 = PushButton(app, command=self.received_grip_callback, args=["Pinch"], text="Pinch")
            grip_4 = PushButton(app, command=self.received_grip_callback, args=["Stop"], text="Stop")
            grip_5 = PushButton(app, command=self.received_grip_callback, args=["Emergency"], text="Emergency")
            grip_6 = PushButton(app, command=self.received_grip_callback, args=["Flat"], text="Flat")
            grip_7 = PushButton(app, command=self.received_grip_callback, args=["Ball"], text="Ball")
            grip_8 = PushButton(app, command=self.received_grip_callback, args=["Fist"], text="Fist")
            grip_9 = PushButton(app, command=self.received_grip_callback, args=["Cup Cycle"], text="Cup Cycle")
            grip_10 = PushButton(app, command=self.received_grip_callback, args=["Hammer Cycle"], text="Hammer Cycle")
            grip_11 = PushButton(app, command=self.received_grip_callback, args=["Pinch Cycle"], text="Pinch Cycle")
            grip_12 = PushButton(app, command=self.received_grip_callback, args=["Flat Cycle"], text="Flat Cycle")
            grip_13 = PushButton(app, command=self.received_grip_callback, args=["Ball Cycle"], text="Ball Cycle")
            grip_14 = PushButton(app, command=self.received_grip_callback, args=["Fist Cycle"], text="Fist Cycle")
            app.display()
        except KeyboardInterrupt:
            pass

    @staticmethod
    def deactivate():
        GRASP_Input_TS.activated = False
        pass
