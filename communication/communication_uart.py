#!/usr/bin/python

from communication.communication import Communication
import serial
from time import sleep


class CommunicationUART(Communication):
    ser = serial.Serial()

    def setup(self):
        # Configure serial port
        self.ser.port = 'COM3'
        self.ser.baudrate = 9600
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.timeout = 1
        # Open serial port
        self.ser.open()
        super(CommunicationUART, self).setup()
        pass

    def receive_callback(self):
        x = self.ser.read(1)  # reads in byte form
        print(x)
        g = int.from_bytes(x, byteorder='big')  # converts byte to integer (Note that if timeout, then 0 is returned)
        print(g)
        super(CommunicationUART, self).receive_callback()
        return g

    def send(self, grip):
        print(grip)
        s = bytes(grip)  # encodes integer as byte
        print(s)  # should show corresponding ascii
        print("bytes written", self.ser.write(s))
        super(CommunicationUART, self).send(grip)
        pass


def main():
    com = CommunicationUART()
    com.send([0, 255])
    sleep(1)
    com.receive_callback()
    com.send([3, 255])
    sleep(1)
    com.receive_callback()
    # print("received", com.ser.read(1))
    # com.send(255)


if __name__ == '__main__':
    main()
