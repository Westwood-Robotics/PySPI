# PySPI
Sample code for python SPI encoder communication using Raspberry Pi. The sample is specifically built to work with Westwood Robotics MPS encoders, but feel free to modify it to fit other SPI encoders.

## Device
The pinout and dimentions of the Westwood Robotics MPS encoder is as shown below:

![](images/Specs.jpg)

Connect the pins accordingly to your Pi, or any compatible device of your choice.

The connector is a 6-pos JST connector with part # BM06B-SRSS-TB(LF)(SN). Board thickness is 1.2mm.

## Dependencies
Install wiringpi and spidev packages before using.

## Usage
1. Add these files into your project and just simply put```from MPS import *```at the beginning of your code and you are good to use this package. Refer to 'sensor_orientation_update.py' and 'simple_read.py' as some sample usage.

2. Even though there are only 2 CS pins for SPI communication on Pi, you can still link more than 2 devices by using GPIO pins as CS pins. When doing so, please set ```gpio``` to ```True``` when creating an ```MPS_Encoder``` instance and use GPIO numbering for your CS pin number.

3. Use ```MPS_Encoder``` with single encoder; use ```MPS_Encoder_Cluster``` if you wish to bundle several encoders using GPIO for ChipSelect.
4. AVOID USING PIN CE0.

Enjoy!
