#!/usr/bin/python

import GRASP_Comm
import GRASP_Input
import threading

from GRASP_Input_TS    import GRASP_Input_TS
from GRASP_Input_Voice import GRASP_Input_Voice
from GRASP_Comm_UART   import GRASP_Comm_UART
from queue             import Queue
from time              import sleep

class GRASP_Manager():
    #FIELDS:------------------------------------------------------------------------------------------------------------
    knownGrips = ['mug', 'pinch', 'ball', 'hammer', 'flat']
    commTimeout = 300.0



    #INITIALIZER:-------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event   ()
        self.ts        = GRASP_Input_TS    (1, "Touch Screen", self.gripQueue)
        self.voice     = GRASP_Input_Voice (2, "Voice", self.gripQueue)
        self.comm      = GRASP_Comm_UART   ()

    #METHODS:-----------------------------------------------------------------------------------------------------------
    def manage(self):
        self.ts    .start()
        self.voice .start()

        try:
            while True:
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
