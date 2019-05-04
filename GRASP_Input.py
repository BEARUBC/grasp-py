#!/usr/bin/python

from abc import ABCMeta

class GRASP_Input(metaclass=ABCMeta)

    @abstractmethod
    def setup()
        pass

    @abstractmethod
    def received_grip_callback()
        pass

    @abstractmethod
    def deactivate()
        pass
