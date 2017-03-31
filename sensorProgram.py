from nanpy import (ArduinoApi, SerialManager)
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensorConnection = SerialManager(device='/dev/ttyUSB0')
A = ArduinoApi(connection=sensorConnection)

laserL = 14
laserR = 15
laserF = 16
laserB = 17

TuSonicL1 = 7
EuSonicL1 = 11

TuSonicL2 = 12
EuSonicL2 = 13

TuSonicR1 = 15
EuSonicR1 = 16

TuSonicR2 = 18
EuSonicR2 = 22

GPIO.setup(TuSonicL1, GPIO.OUT)
GPIO.setup(EuSonicL1, GPIO.IN)
GPIO.setup(TuSonicL2, GPIO.OUT)
GPIO.setup(EuSonicL2, GPIO.IN)
GPIO.setup(TuSonicR1, GPIO.OUT)
GPIO.setup(EuSonicR1, GPIO.IN)
GPIO.setup(TuSonicR2, GPIO.OUT)
GPIO.setup(EuSonicR2, GPIO.IN)


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

def uSonicCalling(b):
  if b == 'L1':
    return uSonicValue(TuSonicL1, EuSonicL1)
  elif b == 'L2':
    return uSonicValue(TuSonicL2, EuSonicL2)
  elif b == 'R1':
    return uSonicValue(TuSonicR1, EuSonicR1)
  elif b == 'R2':
    return uSonicValue(TuSonicR2, EuSonicR2)

  
def uSonicValue(c, d)
    GPIO.output(c, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(c, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(c, GPIO.LOW)
    
    while GPIO.input(d) == 0:
      start = time.time()
      
    while GPIO.input(d) == 1:
      end = time.time()
      
    length = (end-start)*18500
    
    return length
    
