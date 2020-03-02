#!/usr/bin/env python
# coding=utf-8
# Skripte importieren
import drinks as d
import Ausfuerung as Ass
import MFRC522
import signal
# Bibliotheken importieren
import os
import time
import RPi.GPIO as GPIO
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
from PIL import Image

# Display einrichten
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
#rfid setup
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()

GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN, pull_up_down = GPIO.PUD_UP)
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)

# Ein paar Abkürzungen, um den Code zu entschlacken
draw = oled.canvas
# Schriftarten festlegen
FreeSans12 = ImageFont.truetype('FreeSans.ttf', 23)
FreeSans13 = ImageFont.truetype('FreeSans.ttf', 18)
FreeSans14 = ImageFont.truetype('FreeSans.ttf', 17)
FreeSans20 = ImageFont.truetype('FreeSans.ttf', 50)
# Display zum Start löschen


        
      
def nohomo():
    menupunkt = ['Cocktails','Mischen','Shots', 'Sets', 'Ausschalten']
    
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.HIGH)
    p = 0
    oled.cls()
    oled.display()
    draw.text((1,1), menupunkt[p], font=FreeSans12, fill=1)
    oled.display()
    try:
        while p < 5:
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            if GPIO.input(16) == False:
                if p == 3:
                    p=-1
                p=p+1
                oled.cls()
                oled.display()
                draw.text((1, 1), menupunkt[p], font=FreeSans12, fill=1)
                oled.display()
            
            if GPIO.input(18) == False:
                if p == 0:
                    cocktails()
                if p == 1:
                    mischen()
                if p == 2:
                    shots()
                if p == 3:
                    import start
                    start.programm()
                if p == 4:
                    oled.cls()
                    draw.text((1,1), "Sicher?", font=FreeSans14, fill=1)
                    draw.text((95, 45), "Ja", font=FreeSans14, fill =1)
                    draw.text((1, 45), "Nein", font=FreeSans14, fill =1)
                    oled.display()
                    while True:
                        if GPIO.input(18) == False:
                            oled.cls()
                            GPIO.cleanup()
                            os.system("sudo shutdown -h now")
                        if GPIO.input(16) == False:
                            nohomo()
            
            if status == MIFAREReader.MI_OK:

                ID = uid[0]+uid[1]+uid[2]+uid[3]
                print (ID)
                if ID == 450:
                    Ass.main(0)
                    nohomo()
            
                if ID == 621:
                    print ("Reinigger")
                    oled.cls()
                    draw.text((34,-11), ".", font=FreeSans14, fill=1)
                    draw.text((38,-11), ".", font=FreeSans14, fill=1)
                    draw.text((1,1), "Schlauche aus",font=FreeSans14, fill=1)
                    draw.text((1,20), "Flaschen",font=FreeSans14, fill=1)
                    draw.text((1,39), "nehmen!",font=FreeSans14, fill=1)
                    draw.text((95, 46), "OK", font=FreeSans14, fill =1)
                    oled.display()
                    while True:
                        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                        (status,uid) = MIFAREReader.MFRC522_Anticoll()
                        if status == MIFAREReader.MI_OK:
                            ID = uid[0]+uid[1]+uid[2]+uid[3]
                            if ID == 621:
                                nohomo()
                        if GPIO.input(18) == False:
                            d.reinigger(1)
                            oled.display()
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
                                    oled.display()
                                    draw.text((1,1), "Reinigung",font=FreeSans12, fill=1)
                                    draw.text((1,30), "lauft...",font=FreeSans12, fill=1)
                                    draw.text((7,16), ".",font=FreeSans12, fill=1)
                                    draw.text((11,16), ".",font=FreeSans12, fill=1)
                                    oled.display()
                                    d.reinigger(2)
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
                                            d.reinigger(1)
                                            nohomo()
                                    

    except KeyboardInterrupt:
        GPIO.cleanup()
        oled.cls()
        oled.display()

def cocktails():
    x = 0
    oled.cls()
    oled.display()
    draw.text((1, 1), d.drinks[x][0], font=FreeSans12, fill=1)
    draw.text((1, 30), d.drinkszwei[x], font=FreeSans12, fill=1)
    oled.display()
    try:
        while x < d.anzahld+1:
            if GPIO.input(16) == False:
                if x == d.anzahld-1:
                    x=-1
                x=x+1
                oled.cls()
                oled.display()
                draw.text((36, -13), d.umlaute[x], font=FreeSans12, fill=1)
                draw.text((40, -13), d.umlaute[x], font=FreeSans12, fill=1)
                draw.text((1, 1), d.drinks[x][0], font=FreeSans12, fill=1)
                draw.text((1, 30), d.drinkszwei[x], font=FreeSans12, fill=1)
                oled.display()
                
            if GPIO.input(18) == False:
                if x<3:
                    Ass.main(x)
                nohomo()
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        oled.cls()
        oled.display()

def mischen():
    alkohol = ["Bacardi", "Tequila","Gin","Vodka"]
    alkohol2 = ["Razz","","",""]
    saft = ["O-Saft", "HMA-Saft"]
    
    gr = 0
    anzahla = 4
    anzahls = 2
    a = 0
    s = 0
    walkohol = ""
    wsaft = ""
    
    oled.cls()
    draw.text((1,1), "Grosse wahlen!", font=FreeSans14, fill=1)
    draw.text((21,-11), ".",font=FreeSans14, fill=1)
    draw.text((25,-11), ".",font=FreeSans14, fill=1)
    draw.text((70,-11), ".",font=FreeSans14, fill=1)
    draw.text((74,-11), ".",font=FreeSans14, fill=1)
    draw.text((1,45), "200 ml", font=FreeSans14, fill=1)
    draw.text((75,45), "300 ml", font=FreeSans14, fill=1)
    oled.display()
    l = 0
    while l == 0:
        if GPIO.input(16) == False:
            gr = 1
            l = 1
        
        if GPIO.input(18) == False:
            gr = 1.5
            l = 1
    
    oled.cls()
    oled.display()
    draw.text((1, 1),  "1. Alkohol", font=FreeSans14, fill=1)
    draw.text((1, 20),  "2. Saft", font=FreeSans14, fill=1)
    draw.text((0, 45), "Abbruch", font=FreeSans14, fill=1)
    draw.text((95, 45), "OK", font=FreeSans14, fill =1)
    oled.display()
    
    w=0
    while w==0:
        if GPIO.input(16) == False:
            nohomo()
        
        if GPIO.input(18) == False:
            oled.cls()
            oled.display()
            draw.text((1, 1), alkohol[a], font=FreeSans12, fill=1)
            draw.text((1, 30), alkohol2[a], font=FreeSans12, fill=1)
            oled.display()
            while a<4:
                if GPIO.input(16) == False:
                    if a == anzahla-1:
                        a=-1
                    a=a+1
                    oled.cls()
                    oled.display()
                    draw.text((1, 1), alkohol[a], font=FreeSans12, fill=1)
                    draw.text((1, 30), alkohol2[a], font=FreeSans12, fill=1)
                    oled.display()
                
                if GPIO.input(18) == False:
                    walkohol = alkohol[a]+" "+alkohol2[a]
                    oled.cls()
                    oled.display()
                    draw.text((1, 1), saft[s], font=FreeSans12, fill=1)
                    oled.display()
                    while s<2:
                        if GPIO.input(16) == False:
                            if s == anzahls-1:
                                s=-1
                            s=s+1
                            oled.cls()
                            oled.display()
                            draw.text((1, 1), saft[s], font=FreeSans12, fill=1)
                            oled.display()
                        
                        if GPIO.input(18) == False:
                            wsaft = saft[s]
                            oled.cls()
                            draw.text((1,1), walkohol, font=FreeSans14, fill=1)
                            draw.text((1,25), wsaft, font=FreeSans14, fill=1)
                            draw.text((0, 46), "Abbruch", font=FreeSans14, fill=1)
                            draw.text((95, 46), "OK", font=FreeSans14, fill =1)
                            oled.display()
                            while True:
                                if GPIO.input(16) == False:
                                    nohomo()
                                
                                if GPIO.input(18) == False:
                                    GPIO.output(led1, GPIO.HIGH)
                                    GPIO.output(led2, GPIO.LOW)
                                    GPIO.output(led3, GPIO.HIGH)
                                    oled.cls()
                                    if walkohol == 'Bacardi Razz':
                                        GPIO.output(Pumpe1, GPIO.LOW)
                                        draw.bitmap((0, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Rum.png'), fill=1)
                                    if walkohol == 'Tequila ':
                                        GPIO.output(Pumpe2, GPIO.LOW)
                                        draw.bitmap((0, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Tequila.png'), fill=1)
                                    if walkohol == 'Gin ':
                                        GPIO.output(Pumpe3, GPIO.LOW)
                                        draw.bitmap((0, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Gin.png'), fill=1)
                                    if walkohol == 'Vodka ':
                                        GPIO.output(Pumpe4, GPIO.LOW)
                                        draw.bitmap((0, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Vodka.png'), fill=1)
                                    if wsaft == 'O-Saft':
                                        GPIO.output(Pumpe5, GPIO.LOW)
                                        draw.bitmap((50, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Orange.png'), fill=1)
                                    if wsaft == 'HMA-Saft':
                                        GPIO.output(Pumpe6, GPIO.LOW)
                                        draw.bitmap((50, 0), Image.open('/home/pi/Desktop/lib_oled96test2/pi_logo.png'), fill=1)
                                    oled.display()
                                    time.sleep(30*gr)
                                    for i in xrange(0,4):
                                        GPIO.output(apumpe[i], GPIO.HIGH)
                                    time.sleep(30*gr)
                                    for d in xrange(0,2):
                                        GPIO.output(spumpe[d], GPIO.HIGH)
                                    oled.cls()
                                    draw.bitmap((32, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Cocktail.png'), fill=1)
                                    oled.display()
                                    GPIO.output(led1, GPIO.HIGH)
                                    GPIO.output(led2, GPIO.HIGH)
                                    GPIO.output(led3, GPIO.LOW)
                                    time.sleep(6)
                                    nohomo()
                                   
def shots():
    alk = ["Bacardi", "Tequila","Gin","Vodka", "Zuruck"]
    alk2 = ["Razz","","","",""]
    umlaut = ["","","","","."]
    a=0
    anzahla = 5
    
    oled.cls()
    oled.display()
    draw.text((1, 1), alk[a], font=FreeSans12, fill=1)
    draw.text((1, 30), alk2[a], font=FreeSans12, fill=1)
    oled.display()
    while a<5:
        if GPIO.input(16) == False:
            if a == anzahla-1:
                a=-1
            a=a+1
            oled.cls()
            oled.display()
            draw.text((36, -13), umlaut[a], font=FreeSans12, fill=1)
            draw.text((40, -13), umlaut[a], font=FreeSans12, fill=1)
            draw.text((1, 1), alk[a], font=FreeSans12, fill=1)
            draw.text((1, 30), alk2[a], font=FreeSans12, fill=1)
            oled.display()
            
        if GPIO.input(18) == False:
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.HIGH)
            if a == 0:
                oled.cls()
                draw.bitmap((26, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Rum.png'), fill=1)
                oled.display()
                GPIO.output(Pumpe1, GPIO.LOW)
                time.sleep(9.1)
                GPIO.output(Pumpe1, GPIO.HIGH)
            if a == 1:
                oled.cls()
                draw.bitmap((26, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Tequila.png'), fill=1)
                oled.display()
                GPIO.output(Pumpe2, GPIO.LOW)
                time.sleep(9.1)
                GPIO.output(Pumpe2, GPIO.HIGH)
            if a == 2:
                oled.cls()
                draw.bitmap((26, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Gin.png'), fill=1)
                oled.display()
                GPIO.output(Pumpe3, GPIO.LOW)
                time.sleep(9.1)
                GPIO.output(Pumpe3, GPIO.HIGH)
            if a == 3:
                oled.cls()
                draw.bitmap((26, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Vodka.png'), fill=1)
                oled.display()
                GPIO.output(Pumpe4, GPIO.LOW)
                time.sleep(9.1)
                GPIO.output(Pumpe4, GPIO.HIGH)
            if a == 4:
                nohomo()
            
            nohomo()