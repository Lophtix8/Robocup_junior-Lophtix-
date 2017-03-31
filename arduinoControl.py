from nanpy import (ArduinoApi, SerialManager)
import RPi.GPIO as GPIO
from motorProgram import *
from sensorProgram import *
from mappingProgram import *

connection = SerialManager(device='/dev/ttyUSB0')
a = ArduinoApi(connection=connection)

map = {x + ',' + y: start}

while running == True:
  laserValue('L')
  laserValue('R')
  laserValue('F')
  laserValue('B')
  Mapping()
