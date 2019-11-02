#!/usr/bin/python

from builtins    import staticmethod, KeyboardInterrupt
from GRASP_Input import GRASP_Input
from guizero     import App, Text, PushButton
from time        import sleep



class GRASP_Input_TS(GRASP_Input):
    #FIELDS:------------------------------------------------------------------------------------------------------------
    activated = True



    #INITIALIZER:-------------------------------------------------------------------------------------------------------



    #METHODS:-----------------------------------------------------------------------------------------------------------
    @staticmethod
    def reactivate():
        GRASP_Input_TS.activated = True
        pass

    def received_grip_callback(self, grip):
        if GRASP_Input_TS.activated:
            self.grip.value = grip
            self.queue.put(grip)
        else:
            print("Blocked.")

    def setup(self):
        pass
    def run(self):
        try:
            print("Start Touch Screen.")
            app = App(title="Hello, world!")
            self.grip_message = Text(app, text="No Grip Selected.")
            grip_1 = PushButton(app, command=self.received_grip_callback, args=["Cup"], text="Cup")
            app.display()
        except KeyboardInterrupt:
            pass

    @staticmethod
    def deactivate():
        GRASP_Input_TS.activated = False
