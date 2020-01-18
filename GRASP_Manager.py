#!/usr/bin/python

import GRASP_Comm
import GRASP_Input
import threading
import serial

from GRASP_Input_TS    import GRASP_Input_TS
from GRASP_Input_Voice import GRASP_Input_Voice
from GRASP_Comm_UART   import GRASP_Comm_UART
from queue             import Queue
from time              import sleep

class GRASP_Manager():

    knownGrips = ['Cup', 'Hammer', 'Pinch', 'Flat', 'Ball', 'Fist', 'Cup Cycle', 'Hammer Cycle', 'Pinch Cycle', 'Flat Cycle', 'Ball Cycle', 'Fist Cycle', 'SAFETY_OFF', 'Stop', 'Emergency','Rigid','Distance']
    commTimeout = 300.0
    uiSafetyOn = True



    #INITIALIZER:-------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event   ()
        self.ts        = GRASP_Input_TS    (1, "Touch Screen", self.gripQueue)
        self.voice     = GRASP_Input_Voice (2, "Voice", self.gripQueue)
        self.comm      = GRASP_Comm_UART   ()
    def manage(self):
        self.ts    .start()
        self.voice .start()

        try:
            while True:
                
                uiOnOrOff = self.comm.receive_callback()

                if uiOnOrOff == 8:
                    uiSAfetyOn = False

                elif uiOnOrOff == 9:
                    uiSafetyOn = True

                grip = self.gripQueue.get(block=True)

                print("Grip is: ", grip)

                if grip.strip().lower() in GRASP_Manager.knownGrips:
                    GRASP_Input_TS    .deactivate()
                    GRASP_Input_Voice .deactivate()

                    print(grip, "Sending.")
                    self.comm.send(grip)

                    GRASP_Input_TS    .reactivate()
                    GRASP_Input_Voice .reactivate()

        except KeyboardInterrupt:
            print("Cancelled")
            self.ts    .join()
            self.voice .join()
