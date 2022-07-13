#!/usr/bin/env python
'''
Reads the value from the wired heart rate monitor
'''
#import GPIO Lib
import time
from Jetson import GPIO

OUTPUT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
curr_value = GPIO.LOW
try:
    while True:
        time.sleep(1)
        GPIO.output(OUTPUT_PIN, curr_value)
        curr_value ^= GPIO.HIGH
finally:
    GPIO.cleanup()
