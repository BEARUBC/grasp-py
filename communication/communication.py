#!/usr/bin/python

from abc import ABCMeta, abstractmethod


# Abstract class for Nucleo communication
class Communication(metaclass=ABCMeta):
    def __init__(self):
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def receive_callback(self):
        print("received")
        pass

    @abstractmethod
    def send(self, grip):
        ## Wait for response
        # Temp:
        print("sent")
        # sleep(5)
        # self.receive_callback()
        pass
