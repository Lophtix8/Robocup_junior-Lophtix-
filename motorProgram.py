from nanpy import (ArduinoApi, SerialManager)

motorConnection = SerialManager(device='motor arduino')
A = ArduinoApi(connection='motorConnection')

