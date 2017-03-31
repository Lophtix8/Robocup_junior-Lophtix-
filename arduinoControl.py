#!/usr/local/bin/python3
from nanpy import (ArduinoApi, SerialManager)
import RPi.GPIO as GPIO
from motorProgram import *
from sensorProgram import *
from mappingProgram import *

connection = SerialManager(device='/dev/ttyUSB0')
a = ArduinoApi(connection=connection)

laserL = laserValue('L')
laserR = laserValue('R')
laserF = laserValue('F')
laserB = laserValue('B')

map = {x + ',' + y: start}

while running == True:
  Mapping(laserL, laserR, laserF, laserB)
