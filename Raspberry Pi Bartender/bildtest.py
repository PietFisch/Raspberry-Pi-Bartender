#!/usr/bin/env python
# coding=utf-8
 
# Bibliotheken importieren
import time
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import Image
from PIL import ImageFont
 
# Display einrichten
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
FreeSans14 = ImageFont.truetype('FreeSans.ttf', 17)
FreeSans12 = ImageFont.truetype('FreeSans.ttf', 23)

# Ein paar Abkürzungen, um den Code zu entschlacken
draw = oled.canvas
 
# Display zum Start löschen
oled.cls()
draw.text((36, -13), '.', font=FreeSans12, fill=1)
draw.text((40, -13), '.', font=FreeSans12, fill=1)
draw.text((1, 1), 'Zuruck', font=FreeSans12, fill=1)
oled.display()
