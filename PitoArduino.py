"""Serial connection between Raspberry Pi and Arduino"""

import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

# write to serial
ser.write("R")

ser.close()