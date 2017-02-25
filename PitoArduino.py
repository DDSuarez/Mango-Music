"""Serial connection between Raspberry Pi and Arduino"""

import time
import serial

# might have to do a 'sudo chmod a+rw /dev/ttyUSB0'
# for the pi /dev/ttyUSB0
ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

# write to serial
ser.write("R")

ser.close()