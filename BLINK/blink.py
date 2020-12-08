import RPi.GPIO as GPIO
import time
pin=40 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)
a=0
while True:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.5)
GPIO.cleanup()
