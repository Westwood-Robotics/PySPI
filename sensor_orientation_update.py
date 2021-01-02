#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

# Use this code to update sensor orientation setting.

from MPS import *

# We only have SPI bus 0 available to us on the Pi
bus = 0
# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0
max_speed_hz = 2000
spi_mode = 0
orientation = 0b10

MA310 = MPS_Encoder("MA310", bus, device, max_speed_hz, spi_mode)
MA310.connect()
check = MA310.write_reg('sensor_orientation', orientation)
if check:
    print("Sensor orientation updated.")
else:
    print("Failed to update sensor orientation.")
MA310.release()




