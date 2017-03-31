#!/usr/local/bin/python3
from nanpy import (ArduinoApi, SerialManager)
import time

motorConnection = SerialManager(device=/dev/ttyUSB0)
A = ArduinoApi(connection=motorConnection)

mLeft1 = 'input1'
mLeft2 = 'input2'
eLeft = 'Enable1'

mRight1 = 'input3'
mRight2 = 'input4'
eRight = 'Enable2'

A.pinMode(mLeft1, A.OUTPUT)
A.pinMode(mLeft2, A.OUTPUT)
A.pinMode(eLeft2, A.OUTPUT)

A.pinMode(mRight1, A.OUTPUT)
A.pinMode(mRight2, A.OUTPUT)
A.pinMode(eRight, A.OUTPUT)

