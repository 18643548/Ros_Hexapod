import serial
import time

ser = serial.Serial(
    port= '/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

while 1:
    ser.write("#1P1500#2P1500#3P1500\r\n")
    time.sleep(2)