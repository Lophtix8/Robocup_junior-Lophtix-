#!/usr/local/bin/python3
import serial
global US
US = []
ser = serial.Serial('/dev/ttyUSB0', 9600)

def serialWrite(a):
    ser.write(str(a).encode('utf-8'))

serialWrite(4)
for i in range(6):
    US.append(int(ser.readline(), 10))
    
print(US)
