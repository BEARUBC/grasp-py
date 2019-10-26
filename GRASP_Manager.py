#!/usr/bin/python

import GRASP_Comm
import GRASP_Input
from GRASP_Input_TS import GRASP_Input_TS
from GRASP_Input_Voice import GRASP_Input_Voice
from GRASP_Comm_UART import GRASP_Comm_UART
import threading
from queue import Queue
from time import sleep

class GRASP_Manager():
    knownGrips = ['sea', 'pinch', 'ball', 'hammer', 'flat', 'SAFETY_OFF']
    #knownGrips = ['Cup', 'Hammer', 'Pinch', 'Flat', 'Ball', 'Fist', 'Cup Cycle', 'Hammer Cycle', 'Pinch Cycle', 'Flat Cycle', 'Ball Cycle', 'Fist Cycle', 'SAFETY_OFF', 'Stop', 'Emergency']
    commTimeout = 300.0
    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event()
        self.ts = GRASP_Input_TS(1, "Touch Screen", self.gripQueue) # using input super constructor goes into touchscreen -------------------------------
        self.voice = GRASP_Input_Voice(2, "Voice", self.gripQueue)
        self.comm = GRASP_Comm_UART()
    def manage(self):
        self.ts.start()
        self.voice.start()
        try:
            while(True):
                grip = self.gripQueue.get(block=True)
                print("grip is: ", grip)
                if grip.strip().lower() in GRASP_Manager.knownGrips:
                    GRASP_Input_TS.deactivate()
                    GRASP_Input_Voice.deactivate()
                    print(grip, "sending")
                    self.comm.send(grip)        # uses UART -------------------------------------------------------------------                       
                    GRASP_Input_TS.reactivate()
                    GRASP_Input_Voice.reactivate()

        except KeyboardInterrupt:
            print("Cancelled")
        # self.ts.join()
            self.voice.join()
