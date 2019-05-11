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
    knownGrips = ['cup', 'pincer', 'ball', 'hammer', 'vulcan']
    commTimeout = 300.0
    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event()
        self.ts = GRASP_Input_TS(1, "Touch Screen", self.gripQueue)
        self.voice = GRASP_Input_Voice(2, "Voice", self.gripQueue)
        self.comm = GRASP_Comm_UART()
    def manage(self):
        self.ts.start()
        self.voice.start()
        try:
            while(True):
                grip = self.gripQueue.get(block=True)
                if grip.lower() in GRASP_Manager.knownGrips:
                    GRASP_Input_TS.deactivate()
                    GRASP_Input_Voice.deactivate()
                    print(grip, "sending")
                    self.comm.send(grip)
                    GRASP_Input_TS.reactivate()
                    GRASP_Input_Voice.reactivate()

        except KeyboardInterrupt:
            print("Cancelled")
        # self.ts.join()
        # self.voice.join()
