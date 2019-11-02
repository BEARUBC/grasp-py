#!/usr/bin/python

from abc       import ABCMeta, abstractmethod
from threading import Thread
from time      import sleep



class GRASP_Comm(metaclass=ABCMeta):
    #FIELDS:------------------------------------------------------------------------------------------------------------



    #INITIALIZER:-------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.setup()



    #METHODS:-----------------------------------------------------------------------------------------------------------
    @abstractmethod
    def setup            (self)      :
        print("Setting up.")
        pass

    @abstractmethod
    def receive_callback (self)      :
        print("Callback received.")
        pass

    @abstractmethod
    def send             (self,grip) :
        ## Wait for response
        #Temp:
        print("Sent.")
        # sleep(5)
        # self.receive_callback()
        pass
