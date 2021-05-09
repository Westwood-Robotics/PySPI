import spidev
import wiringpi
import time

max_speed_hz = 2000
spi_mode = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = max_speed_hz
spi.mode = spi_mode
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(22, 1)
wiringpi.digitalWrite(22, 1)  # Set ChipSelect GPIO as HIGH
print("Device connected.")

wiringpi.digitalWrite(22, 0)
send = 0x1E
spi.writebytes([send])
time.sleep(0.005)
wiringpi.digitalWrite(22, 1)

print("RST done.")

PROM_Add = [0xA2, 0xA4, 0xA6, 0xA8, 0xAA, 0xAC]
PROM_readout = []
for add in PROM_Add:
    wiringpi.digitalWrite(22, 0)
    spi.writebytes([add])
    PROM_readout.append(spi.readbytes(2))
    wiringpi.digitalWrite(22, 1)
    # time.sleep(0.001)

print(PROM_readout)
