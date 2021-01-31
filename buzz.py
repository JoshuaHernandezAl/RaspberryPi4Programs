#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BOARD)
#Set buzzer - pin 23 as output
buzzer=16
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
a=0
while a<1:
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(0.25) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    sleep(0.25)
    a+=1
GPIO.cleanup()