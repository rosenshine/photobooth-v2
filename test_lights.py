import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
print "LED on"
GPIO.output(10,GPIO.HIGH)
time.sleep(10)
print "LED off"
GPIO.output(10,GPIO.LOW)
