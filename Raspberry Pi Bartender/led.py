
# Bibliotheken importieren
import time
import RPi.GPIO as GPIO

# Display einrichten
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

pumpen = [Pumpe1, Pumpe2, Pumpe3, Pumpe4, Pumpe5, Pumpe6]

def test():
    for i in range(0,6):
        GPIO.output(pumpen[i], GPIO.LOW)
        time.sleep(0.1)
    time.sleep(13)
    for w in range(0,6):
        GPIO.output(pumpen[w], GPIO.HIGH)
        

test()
GPIO.cleanup()