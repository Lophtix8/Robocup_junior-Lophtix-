from nanpy import (ArduinoApi, SerialManager)

motorConnection = SerialManager(device=/dev/ttyUSB0)
A = ArduinoApi(connection=motorConnection)

