#!/usr/bin/env python
import serial
import time

ser = serial.Serial(
    port= '/dev/ttyAM0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

while 1:
    ser.write("#1P1500#2P1500#3P1500\r\n")
    time.sleep(2)