#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

# Read angles from all three encoders on DT02

from MPS import *
import os

# We only have SPI bus 0 available to us on the Pi
bus = 0
# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = [22, 27, 17]
max_speed_hz = 2000
spi_mode = 0

DT02 = MPS_Encoder_Cluster("MA310", bus, device, max_speed_hz, spi_mode)
DT02.connect()
time.sleep(1)
data = DT02.read_angle()
print(data)


