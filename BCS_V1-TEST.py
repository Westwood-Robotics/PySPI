import spidev
import wiringpi
import time

max_speed_hz = 2000
spi_mode = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = max_speed_hz
spi.mode = spi_mode
print("Device connected.")

send = 0x1E
spi.writebytes([send])
data = spi.readbytes(2)

print(data)