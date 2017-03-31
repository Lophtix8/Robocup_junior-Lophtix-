from nanpy import (ArduinoApi, SerialManager)

sensorConnection = SerialManager(device='/dev/ttyUSB0')
A = ArduinoApi(connection=sensorConnection)

laserL = 14
laserR = 15
laserF = 16
laserB = 17


A.pinMode(laserL, INPUT)
A.pinMode(laserR, INPUT)
A.pinMode(laserF, INPUT)
A.pinMode(laserB, INPUT)

def laserValue(a):
  if a == 'L':
    length = (A.analogRead(laserL)'Equation')
    return length
  elif a == 'R':
    length = (A.analogRead(laserR)'Equation')
    return length
  elif a == 'F':
    length = (A.analogRead(laserF)'Equation')
    return length
  elif a == 'B':
    length = (A.analogRead(laserB)'Equation')
    return length

