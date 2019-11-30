#!/usr/bin/python

import serial
from GRASP_Comm import GRASP_Comm
from time       import sleep



class GRASP_Comm_UART(GRASP_Comm):
    #FIELDS:----------------------------------------------------------------------------------------------------------



    #INITIALIZER:-------------------------------------------------------------------------------------------------------



    #METHODS:-----------------------------------------------------------------------------------------------------------
    def setup(self):
        # Configure serial port

        # From Raunak's Branch:
        # self.ser.port     = '/dev/ttyACM0'
        # self.ser.baudrate = 115200
        # self.ser.parity   = serial.PARITY_NONE
        # self.ser.stopbits = serial.STOPBITS_ONE
        # self.ser.bytesize = serial.EIGHTBITS
        # self.ser.timeout  = 1
        self.ser = serial.Serial() 
        self.ser.port='COM3'
        self.ser.baudrate=9600
        self.ser.parity=serial.PARITY_NONE #default set up
        self.ser.stopbits=serial.STOPBITS_ONE
        self.ser.bytesize=serial.EIGHTBITS  
        self.ser.timeout=1

        # Open serial port
        self.ser.open()
        super(GRASP_Comm_UART,self).setup()
        pass

    def receive_callback(self):
        x = self.ser.read(1) #reads in byte form
        g = int.from_bytes(x, byteorder='big') #converts byte to integer (Note that if timeout, then 0 is returned)

        print(x)
        print(g)

        super(GRASP_Comm_UART,self).receive_callback()
        
        return g

    def send(self,grip):
        print(grip)
        s = bytes(grip) # encodes integer as byte
        print(s) # should show corresponding ascii
        print("bytes written", self.ser.write(s))
        super(GRASP_Comm_UART,self).send(grip) # sends -------------------------------------------------------------
        pass



#MAIN:------------------------------------------------------------------------------------------------------------------
def main():
    com = GRASP_Comm_UART()
    com.send([0, 255])
    sleep(1)
    com.receive_callback()
    com.send([3, 255])
    sleep(1)
    com.receive_callback()
    print("received", com.ser.read(1))
    com.send(255)
if __name__ == '__main__':
    main()
