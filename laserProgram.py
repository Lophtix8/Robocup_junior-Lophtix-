from nanpy import (ArduinoApi, SerialManager)

sensorConnection = SerialManager(device='laser arduino')
A = ArduinoApi(connection=sensorConnection)

laserL = A5
laserR = A4
laserF = A3
laserB = A2


A.pinMode(laserL, INPUT)
A.pinMode(laserR, INPUT)
A.pinMode(laserF, INPUT)
A.pinMode(laserB, INPUT)

def laserValue(a)
  if a == 'L':
    return A.analogRead(laserL)
  elif a == 'R':
    return A.analogRead(laserR)
  elif a == 'F':
    return A.analogRead(laserF)
  elif a == 'B':
    return A.analogRead(laserB)

