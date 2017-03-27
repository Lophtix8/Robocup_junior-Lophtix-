from nanpy import ArduinoApi, SerialManager
import laserProgram

laserConnection = SerialManager(device='laser arduino')
gripperConnection = SerialManager(device='gripper arduino')

laserA = ArduinoApi(connection=laserConnection)
motorA = ArduinoApi(connection=motorConnection)

laserL = A5
laserR = A4
laserF = A3
laserB = A2



laserA.pinMode(laserL, INPUT)
laserA.pinMode(laserR, INPUT)
laserA.pinMode(laserF, INPUT)
laserA.pinMode(laserB, INPUT)

