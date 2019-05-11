#!/usr/bin/python

from GRASP_Comm import GRASP_Comm

class GRASP_Comm_UART(GRASP_Comm):

    def setup(self):
        pass

    def receive_callback(self):
        super().receive_callback()
        pass

    def send(self, grip):
        super().send(grip)
        pass
