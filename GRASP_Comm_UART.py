#!/usr/bin/python

from GRASP_Comm import GRASP_Comm
import serial

class GRASP_Comm_UART(GRASP_Comm):

    ser = serial.Serial()

    def setup(self):
        # Configure serial port
        self.ser.port='COM4'
        self.ser.baudrate=9600
        self.ser.parity=serial.PARITY_NONE
        self.ser.stopbits=serial.STOPBITS_ONE
        self.ser.bytesize=serial.EIGHTBITS
        self.ser.timeout=1
        # Open serial port
        self.ser.open()
        super(GRASP_Comm_UART,self).setup()
        pass

    def receive_callback(self):
        x = self.ser.read(1) #reads in byte form
        print(x)
        g = int.from_bytes(x, byteorder='big') #converts byte to integer (Note that if timeout, then 0 is returned)
        print(g)
        super(GRASP_Comm_UART,self).receive_callback()
        pass

    def send(self,grip):
        print(grip)
        s = bytes(grip) # encodes integer as byte
        print(s) # should show corresponding ascii
        self.ser.write(s)
        super(GRASP_Comm_UART,self).send(grip)
        pass


def main():
    com = GRASP_Comm_UART()
    com.send(0)

if __name__ == '__main__':
    main()