from motorProgram import *
from sensorProgram import *
from mappingProgram import *

map = {x + ',' + y: start}

while running == True:
  laserValue('L')
  laserValue('R')
  laserValue('F')
  laserValue('B')
  mappingProgram
