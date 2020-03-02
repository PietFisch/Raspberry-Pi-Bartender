#!/usr/bin/env python

from lib_oled96 import ssd1306

from smbus import SMBus
i2cbus = SMBus(1)        # 1 = Raspberry Pi but NOT early REV1 board

oled = ssd1306(i2cbus)   # create oled object, nominating the correct I2C bus, default address

# we are ready to do some output ...

# put border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

# Write two lines of text.
draw.bitmap((32, 0), Image.open('Cocktail.png'), fill=1)

# now display that canvas out to the hardware
oled.display()
