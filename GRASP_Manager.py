#!/usr/bin/python

import GRASP_Comm
import GRASP_Input
import threading
import json

# from GRASP_Input_TS import GRASP_Input_TS
import GRASP_gui as gui
from GRASP_Input_Voice import GRASP_Input_Voice
from GRASP_Comm_UART import GRASP_Comm_UART
from queue             import Queue
from time              import sleep

class GRASP_Manager():
    # Fields:
    knownGrips = ['Cup', 'Hammer', 'Pinch', 'Flat', 'Ball', 'Fist', 'Cup Cycle', 'Hammer Cycle', 'Pinch Cycle', 'Flat Cycle', 'Ball Cycle', 'Fist Cycle', 'SAFETY_OFF', 'Stop', 'Emergency']
    commTimeout = 300.0


    ## Constructor:
    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event()
        # self.ts        = GRASP_Input_TS(1, "Touch Screen", self.gripQueue)
        self.voice     = GRASP_Input_Voice(2, "Voice", self.gripQueue)
        self.comm      = GRASP_Comm_UART()
        self.app       = gui()
        app.mainloop()

    ## Methods:
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
                    command = json.dumps('command': grip)
                    self.comm.send(command)

                    GRASP_Input_TS    .reactivate()
                    GRASP_Input_Voice .reactivate()

                dict = self.comm.receive_callback.keys()
                if 'battery' in dict:
                    print("battery percentage:", dict['battery'])
                    if dict['battery'] < 10:
                        self.app.shutdown()
                        self.gripQueue.put('Stop')
                if 'fsr' in dict:
                    print("received fsr matrix")
                    FSR(dict['fsr'])


        except KeyboardInterrupt:
            print("Cancelled")
            self.ts    .join()
            self.voice .join()
