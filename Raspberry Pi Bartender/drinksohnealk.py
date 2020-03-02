# Bibliotheken importieren
import time
import RPi.GPIO as GPIO
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
from PIL import Image

#Pumpe definieren
GPIO.setmode(GPIO.BOARD)

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

i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
draw = oled.canvas
#Ingredients:
#    0 = Gin
#    1 = Rum
#    2 = Vodka
#    3 = Tequila
#    4 = Cola
#    5 = O-juice
#drinks = [name],[ingredients],[ml]
anzahld = 4;
drinks = [\
 ["Long Island",[0,1,2,3,4,5],[25,25,25,25,140,60]], 
 ["Raspi",[3,5],[100,200]],
 ["Dry-Dream",[2,5],[100,200]],
 ["Zuruck",[0,1],[25,25]]
 ]
drinkszwei = ["","Cocktail","",""]
umlaute = ["","","","."]
#print(drinks[0][0])
#for x in drinks[y][z]:
#    print (x)

def drinktest():
    GPIO.output(Pumpe1, GPIO.LOW)
    time.sleep(60)
    GPIO.output(Pumpe1, GPIO.HIGH)

def drink0(gr):
    oled.cls()
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas1.png'), fill=1)
    oled.display()
    GPIO.output(Pumpe1, GPIO.LOW)
    GPIO.output(Pumpe4, GPIO.LOW)
    GPIO.output(Pumpe6, GPIO.LOW)
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas2.png'), fill=1)
    oled.display()
    time.sleep(2.15*gr)
    GPIO.output(Pumpe4, GPIO.HIGH)
    GPIO.output(Pumpe3, GPIO.LOW)
    GPIO.output(Pumpe5, GPIO.LOW)
    time.sleep(1.7*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas3.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas4.png'), fill=1)
    oled.display()
    time.sleep(0.45*gr)
    GPIO.output(Pumpe3, GPIO.HIGH)
    GPIO.output(Pumpe5, GPIO.HIGH)
    time.sleep(3.4*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas5.png'), fill=1)
    oled.display()
    time.sleep(2.6*gr)
    GPIO.output(Pumpe1, GPIO.HIGH)
    time.sleep(1.25*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas6.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas7.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas8.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas9.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas10.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas11.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas12.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas13.png'), fill=1)
    oled.display()
    time.sleep(3.85*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas14.png'), fill=1)
    oled.display()
    time.sleep(0.1*gr)
    GPIO.output(Pumpe6, GPIO.HIGH)

def drink1(gr):
    oled.cls()
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas1.png'), fill=1)
    oled.display()
    GPIO.output(Pumpe1, GPIO.LOW)
    GPIO.output(Pumpe5, GPIO.LOW)
    GPIO.output(Pumpe6, GPIO.LOW)
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas2.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas3.png'), fill=1)
    oled.display()
    time.sleep(4.28*gr)
    GPIO.output(Pumpe1,GPIO.HIGH)
    GPIO.output(Pumpe5, GPIO.HIGH)
    time.sleep(1.08*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas4.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas5.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas6.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas7.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas8.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas9.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas10.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas11.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas12.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas13.png'), fill=1)
    oled.display()
    time.sleep(5.36*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas14.png'), fill=1)
    oled.display()
    time.sleep(5.32*gr)
    GPIO.output(Pumpe6, GPIO.HIGH)
    
    
def drink2(gr):
    oled.cls()
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas1.png'), fill=1)
    oled.display()
    GPIO.output(Pumpe1, GPIO.LOW)
    GPIO.output(Pumpe5, GPIO.LOW)
    GPIO.output(Pumpe6, GPIO.LOW)
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas2.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas3.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas4.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas5.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas6.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas7.png'), fill=1)
    oled.display()
    time.sleep(2.84*gr)
    GPIO.output(Pumpe1, GPIO.HIGH)
    GPIO.output(Pumpe5, GPIO.HIGH)
    time.sleep(0.04*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas8.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas9.png'), fill=1)
    oled.display()
    GPIO.output(Pumpe4, GPIO.LOW)
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas10.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas11.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas12.png'), fill=1)
    oled.display()
    time.sleep(1.42*gr)
    GPIO.output(Pumpe4, GPIO.HIGH)
    time.sleep(1.44)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas13.png'), fill=1)
    oled.display()
    time.sleep(2.86*gr)
    draw.bitmap((28, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Glas14.png'), fill=1)
    oled.display()
    time.sleep(2.8*gr)
    GPIO.output(Pumpe6, GPIO.HIGH)

    
def ansaugen():
    GPIO.output(Pumpe1, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe2, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe3, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(Pumpe4, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe5, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe6, GPIO.LOW)

    time.sleep(10)
    
    GPIO.output(Pumpe1, GPIO.HIGH)
    GPIO.output(Pumpe2, GPIO.HIGH)
    GPIO.output(Pumpe3, GPIO.HIGH)
    GPIO.output(Pumpe4, GPIO.HIGH)
    GPIO.output(Pumpe6, GPIO.HIGH)
    GPIO.output(Pumpe5, GPIO.HIGH)

def reinigger(m):
    GPIO.output(Pumpe1, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe2, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe3, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(Pumpe4, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe5, GPIO.LOW)
    #time.sleep(0.1)
    GPIO.output(Pumpe6, GPIO.LOW)

    time.sleep(30*m)
    
    GPIO.output(Pumpe1, GPIO.HIGH)
    GPIO.output(Pumpe2, GPIO.HIGH)
    GPIO.output(Pumpe3, GPIO.HIGH)
    GPIO.output(Pumpe4, GPIO.HIGH)
    GPIO.output(Pumpe6, GPIO.HIGH)
    GPIO.output(Pumpe5, GPIO.HIGH)
def test():
    GPIO.output(Pumpe1, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe1, GPIO.LOW)
    time.sleep(3)
    GPIO.output(Pumpe2, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe2, GPIO.LOW)
    time.sleep(3)
    GPIO.output(Pumpe3, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe3, GPIO.LOW)
    time.sleep(3)
    GPIO.output(Pumpe4, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe4, GPIO.LOW)
    time.sleep(3)
    GPIO.output(Pumpe5, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe5, GPIO.LOW)
    time.sleep(3)
    GPIO.output(Pumpe6, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pumpe6, GPIO.LOW)
    time.sleep(3)

def test2():
    GPIO.output(Pumpe1, GPIO.LOW)
    time.sleep(60)
    GPIO.output(Pumpe1, GPIO.HIGH)
    
GPIO.cleanup()
