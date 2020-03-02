import MFRC522
import signal

import os
import time
import RPi.GPIO as GPIO
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
from PIL import Image

GPIO.setmode(GPIO.BOARD)
led1 = 36
led2 = 38
led3 = 40

GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.LOW)

GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, GPIO.LOW)

GPIO.setup(led3, GPIO.OUT)
GPIO.output(led3, GPIO.HIGH)

Pumpe1 = 29
Pumpe2 = 31
Pumpe3 = 33
Pumpe4 = 35
Pumpe5 = 37
Pumpe6 = 32


GPIO.setup(Pumpe1, GPIO.OUT)
GPIO.output(Pumpe1, GPIO.HIGH)

GPIO.setup(Pumpe2, GPIO.OUT)
GPIO.output(Pumpe2, GPIO.HIGH)

GPIO.setup(Pumpe3, GPIO.OUT)
GPIO.output(Pumpe3, GPIO.HIGH)

GPIO.setup(Pumpe4, GPIO.OUT)
GPIO.output(Pumpe4, GPIO.HIGH)

GPIO.setup(Pumpe5, GPIO.OUT)
GPIO.output(Pumpe5, GPIO.HIGH)

GPIO.setup(Pumpe6, GPIO.OUT)
GPIO.output(Pumpe6, GPIO.HIGH)

pumpen = [Pumpe1, Pumpe2, Pumpe3, Pumpe4, Pumpe5, Pumpe6]

apumpe = [Pumpe1, Pumpe2, Pumpe3, Pumpe4]

spumpe = [Pumpe5, Pumpe6]

GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN, pull_up_down = GPIO.PUD_UP)
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)

draw = oled.canvas
# Schriftarten festlegen
FreeSans12 = ImageFont.truetype('FreeSans.ttf', 23)
FreeSans13 = ImageFont.truetype('FreeSans.ttf', 18)
FreeSans14 = ImageFont.truetype('FreeSans.ttf', 17)
FreeSans20 = ImageFont.truetype('FreeSans.ttf', 50)


def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()
    
def programm():
    oled.cls()
    oled.display()
    draw.text((0, 0), "Karte auf RFID-", font=FreeSans14, fill=1)
    draw.text((0, 17), "Sensor heben!", font=FreeSans14, fill=1)
    oled.display()
    while True:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            ID = uid[0]+uid[1]+uid[2]+uid[3]
            if ID == 251:
                oled.cls()
                oled.display()
                draw.text((0, 0), "Alkohol", font=FreeSans14, fill=1)
                draw.text((0, 45), "Abbruch", font=FreeSans14, fill=1)
                draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                oled.display()
                while True:
                    if GPIO.input(18) == False:
                        import menu as m
                        m.nohomo()
                    if GPIO.input(16) == False:
                        programm()
            if ID == 517:
                oled.cls()
                oled.display()
                draw.text((0, 0), "Alkoholfrei", font=FreeSans14, fill=1)
                draw.text((0, 45), "Abbruch", font=FreeSans14, fill=1)
                draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                oled.display()
                while True:
                    if GPIO.input(18) == False:
                        import menuohnealk
                        menuohnealk.homo()
                    if GPIO.input(16) == False:
                        programm()

oled.cls()
oled.display()
time.sleep(10)
oled.cls()
oled.display()
draw.text((1, 20), "Willkommen", font=FreeSans13, fill=1)
oled.display()
time.sleep(1.5)
draw.text((100, 20), ".", font=FreeSans13, fill=1)
oled.display()
time.sleep(1.5)
draw.text((105, 20), ".", font=FreeSans13, fill=1)
oled.display()
time.sleep(1.5)
draw.text((110, 20), ".", font=FreeSans13, fill=1)
oled.display()
time.sleep(2)



oled.cls()
oled.display()
draw.bitmap((-3, 0), Image.open('/home/pi/Desktop/lib_oled96test2/start.png'), fill=1)
oled.display()
time.sleep(6)

oled.cls()
oled.display()
draw.text((1, 1),  "Pumpen bereit?", font=FreeSans14, fill=1)
draw.text((1, 30), "NEIN          JA", font=FreeSans13, fill=1)
oled.display()
t = 0
k = 0
while k == 0:
    if GPIO.input(16) == False:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led3, GPIO.LOW)
        oled.cls()
        draw.text((61,-11), ".", font=FreeSans14, fill=1)
        draw.text((65,-11), ".", font=FreeSans14, fill=1)
        draw.text((0,0), "1. Vorspulen", font=FreeSans14, fill=1)
        draw.text((0,15), "2. Leeren", font=FreeSans14, fill=1)
        draw.text((0,30), "3. Ansaugen", font=FreeSans14, fill=1)
        draw.text((95, 45), "OK", font=FreeSans14, fill =1)
        oled.display()
        while True:
            if GPIO.input(18) == False:
                oled.cls()
                draw.text((65,-11), ".", font=FreeSans14, fill=1)
                draw.text((69,-11), ".", font=FreeSans14, fill=1)
                draw.text((0, 0), "Alle Schlauche", font=FreeSans14, fill =1)
                draw.text((0, 17), "ins Wasser", font=FreeSans14, fill =1)
                draw.text((0, 34), "legen!", font=FreeSans14, fill =1)
                draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                oled.display()
                while True:
                    if GPIO.input(18) == False:
                        oled.cls()
                        draw.bitmap((32, 0), Image.open('/home/pi/Desktop/lib_oled96test2/pi_logo.png'), fill=1)
                        oled.display()
                        for i in xrange(0,6):
                            GPIO.output(pumpen[i], GPIO.LOW)
                            time.sleep(0.1)
                        time.sleep(45)
                        for y in xrange(0,6):
                            GPIO.output(pumpen[y], GPIO.HIGH)
                        oled.cls()
                        draw.text((65,-11), ".", font=FreeSans14, fill=1)
                        draw.text((69,-11), ".", font=FreeSans14, fill=1)
                        draw.text((0, 0), "Alle Schlauche", font=FreeSans14, fill =1)
                        draw.text((0, 17), "aus dem Wasser", font=FreeSans14, fill =1)
                        draw.text((0, 34), "nehmen!", font=FreeSans14, fill =1)
                        draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                        oled.display()
                        while True:
                            if GPIO.input(18) == False:
                                oled.cls()
                                draw.text((34,-11), ".", font=FreeSans14, fill=1)
                                draw.text((38,-11), ".", font=FreeSans14, fill=1)
                                draw.text((0,0), "Schlauche", font=FreeSans14, fill=1)
                                draw.text((0,17), "werden entleert!", font=FreeSans14, fill=1)
                                oled.display()
                                for i in xrange(0,6):
                                    GPIO.output(pumpen[i], GPIO.LOW)
                                    time.sleep(0.1)
                                time.sleep(30)
                                for w in xrange(0,6):
                                    GPIO.output(pumpen[w], GPIO.HIGH)
                                oled.cls()
                                draw.text((34,-11), ".", font=FreeSans14, fill=1)
                                draw.text((38,-11), ".", font=FreeSans14, fill=1)
                                draw.text((0,0), "Schlauche in", font=FreeSans14, fill=1)
                                draw.text((0,17), "Flaschen", font=FreeSans14, fill=1)
                                draw.text((0,34), "stecken!", font=FreeSans14, fill=1)
                                draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                                oled.display()
                                while True:
                                    if GPIO.input(18) == False:
                                        oled.cls()
                                        draw.text((0, 0), "Ansaugen...", font=FreeSans14, fill =1)
                                        oled.display()
                                        for i in xrange(0,6):
                                            GPIO.output(pumpen[i], GPIO.LOW)
                                            time.sleep(0.1)
                                        time.sleep(13)
                                        for w in xrange(0,6):
                                            GPIO.output(pumpen[w], GPIO.HIGH)
                                        oled.cls()
                                        draw.text((0,0), "Pumpen sind", font=FreeSans14, fill=1)
                                        draw.text((0,17), "bereit!", font=FreeSans14, fill=1)
                                        draw.text((95, 45), "OK", font=FreeSans14, fill =1)
                                        oled.display()
                                        while t == 0:
                                            if GPIO.input(18) == False:
                                                t = 1
                                                k = 1
                                                programm()
                        
                
        #k += 1
    if GPIO.input(18) == False:
        programm()
        

                
                