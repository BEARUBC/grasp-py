#!/usr/bin/python

import GRASP_Comm
import GRASP_Input
from GRASP_Input_TS import GRASP_Input_TS
from GRASP_Input_Voice import GRASP_Input_Voice
import threading
from queue import Queue
from time import sleep

class GRASP_Manager():
    def __init__(self):
        self.gripQueue = Queue()
        self.gripEvent = threading.Event()
        self.ts = GRASP_Input_TS(1, "Touch Screen", self.gripQueue)
        self.voice = GRASP_Input_Voice(2, "Voice", self.gripQueue)
    def manage(self):
        self.ts.start()
        self.voice.start()
        try:
            while(True):
                grip = self.gripQueue.get(block=True)
                print(grip)
        except KeyboardInterrupt:
            print("Cancelled")
        self.ts.join()
        self.voice.join()
