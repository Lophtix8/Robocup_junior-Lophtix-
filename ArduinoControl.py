from nanpy import ArduinoApi, SerialManager

uSonicConnection = SerialManager(device='ultrasonic arduino')
gripperConnection = SerialManager(device='gripper arduino')

uSonicA = ArduinoApi(connection=uSonicConnection)
gripperA = ArduinoApi(connection=gripperConnection)

