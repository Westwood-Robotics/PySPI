#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

# Simply keep reading angular position data from the encoder.

from pyspi.MPS import *

# We only have SPI bus 0 available to us on the Pi
bus = 0
# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0
max_speed_hz = 2000
spi_mode = 0


MA310 = MPS_Encoder("MA310", bus, device, max_speed_hz, spi_mode)
MA310.connect()
time.sleep(1)
run = True
while run:
    try:
        print(MA310.read_angle())
    except:
        run = False
