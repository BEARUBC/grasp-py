#!/usr/bin/python

from GRASP_Comm import GRASP_Comm
import serial

class GRASP_Comm_UART(GRASP_Comm):
    
    ser = serial.Serial()

    def setup(self):
        # Configure serial port
        self.ser.port='/dev/serial0'
        self.ser.baudrate=9600
        self.ser.parity=serial.PARITY_NONE
        self.ser.stopbits=serial.STOPBITS_ONE
        self.ser.bytesize=serial.EIGHTBITS
        self.ser.timeout=1
        # Open serial port
        self.ser.open()
        super().setup()
        pass

    def receive_callback(self):
        self.ser.read()
        super().receive_callback()
        pass

    def send(self, grip):
        self.ser.write(grip)
        super().send(grip)
        pass
