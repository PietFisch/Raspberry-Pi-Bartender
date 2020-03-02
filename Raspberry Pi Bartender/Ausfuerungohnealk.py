#Ingredients:
#    0 = Gin
#    1 = Rum
#    2 = Vodka
#    3 = Tequila
#    4 = Cola
#    5 = O-juice
#importieren
import drinksohnealk as d
import time
import RPi.GPIO as GPIO
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
from PIL import Image
#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)

led1 = 36
led2 = 38
led3 = 40

GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.LOW)

GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, GPIO.LOW)

GPIO.setup(led3, GPIO.OUT)
GPIO.output(led3, GPIO.HIGH)

draw = oled.canvas

# Schriftarten festlegen
FreeSans12 = ImageFont.truetype('FreeSans.ttf', 23)
FreeSans14 = ImageFont.truetype('FreeSans.ttf', 17)
FreeSans20 = ImageFont.truetype('FreeSans.ttf', 50)

#methoden

def main(y):
    gr = 0
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
    
    z = 3
    while z != 0:
        oled.cls()
        oled.display()
        draw.text((48, 6), str(z), font=FreeSans20, fill=1)
        oled.display()
        time.sleep(1)
        z=z-1
    if GPIO.input(16) == False:
        if GPIO.input(18) == False:
            oled.cls()
            oled.display()
            draw.text((1, 1), "Reinigger...", font=FreeSans12, fill=1)
            oled.display()
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(led3, GPIO.LOW)
            d.reinigger()
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.HIGH)
            
            
        else:
            oled.cls()
            oled.display()
            draw.text((1, 1), "Abbruch...", font=FreeSans12, fill=1)
            oled.display()
            time.sleep(3)
            
        
        
    else:
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.HIGH)
        if y == 0:
            oled.cls()
            oled.display()
            d.drink0(gr)
        if y == 1:
            oled.cls()
            oled.display()
            d.drink1(gr)
        if y == 2:
            oled.cls()
            oled.display()
            d.drink2(gr)
        oled.cls()
        oled.display()
        draw.bitmap((32, 0), Image.open('/home/pi/Desktop/lib_oled96test2/Cocktail.png'), fill=1)
        oled.display()
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led3, GPIO.LOW)
        time.sleep(6)
        
#me.main()


#oled.cls()
#oled.display()
#draw.text((1, 1), d.drinks[y][0], font=FreeSans12, fill=1)
#draw.text((1, 30), str(d.drinks[y][1]), font=FreeSans12, fill=1)
#oled.display()
#time.sleep(5)
