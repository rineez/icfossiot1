#!/usr/bin/env python

import serial

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=0.2)
# ttyACM0 is the arduino device ID

while True:
        rcv = port.readline()
        # rcv has got the information saved
        print "Tag detected:"+rcv
        # it is printed
        


