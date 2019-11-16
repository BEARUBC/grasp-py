#!/usr/bin/python

from abc       import ABCMeta, abstractmethod
from builtins  import staticmethod
from threading import Thread



class GRASP_Input(Thread, metaclass=ABCMeta):
    def __init__(self, threadID, name, queue): #super constructor used for TS_input
        Thread.__init__(self, daemon=True)

        self.threadID = threadID
        self.name     = name
        self.grip     = ""
        self.queue    = queue

        self.setup()



    # METHODS:-----------------------------------------------------------------------------------------------------------
    @abstractmethod
    def run                    (self)      :
        pass
    @abstractmethod
    def setup                  (self)      :
        pass
    @abstractmethod
    def received_grip_callback (self,grip) :
        pass
    @staticmethod
    @abstractmethod
    def deactivate             ()          :
        pass
    @staticmethod
    @abstractmethod
    def reactivate             ()          :
        pass
