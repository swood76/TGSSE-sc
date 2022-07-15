#!/usr/bin/env python
'''
A very simple script to get data from the distance sensor
'''
from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(23, 24)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
