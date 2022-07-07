#import GPIO Lib
import time
import Jetson.GPIO as GPIO


output_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
curr_value = GPIO.LOW
try:
    while True:
        time.sleep(1)
        GPIO.output(output_pin, curr_value)
        curr_value ^= GPIO.HIGH
finally:
    GPIO.cleanup()
