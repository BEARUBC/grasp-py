#!/usr/bin/python

from interaction.interaction_touchscreen import InteractionTouchscreen
from interaction.interaction_voice import InteractionVoice
from communication.communication_uart import CommunicationUART
import threading
from queue import Queue


class Manager:
    knownGrips = ['sea', 'pinch', 'ball', 'hammer', 'flat']
    commTimeout = 300.0

    def __init__(self):
        self.gripQueue = Queue()
        self.commEvent = threading.Event()
        self.ts = InteractionTouchscreen(1, "Touch Screen", self.gripQueue)
        self.voice = InteractionVoice(2, "Voice", self.gripQueue)
        self.comm = CommunicationUART()

    def manage(self):
        self.ts.start()
        self.voice.start()
        try:
            while True:
                grip = self.gripQueue.get(block=True)
                print("grip is: ", grip)
                if grip.strip().lower() in Manager.knownGrips:
                    InteractionTouchscreen.deactivate()
                    InteractionVoice.deactivate()
                    print(grip, "sending")
                    self.comm.send(grip)
                    InteractionTouchscreen.reactivate()
                    InteractionVoice.reactivate()

        except KeyboardInterrupt:
            print("Cancelled")
            # self.ts.join()
            self.voice.join()
