#!/usr/bin/env python
'''
This script subscribes to both the HeartRate and BoundingBox
topics and prints the data it receives to the terminal
'''
import time
import paho.mqtt.client as mqtt

def on_message(message):
    '''
    Decodes the received text and prints it to the console
    '''
    print("received message: " ,str(message.payload.decode("utf-8")))

MQTT_BROKER = "150.250.106.147"

client = mqtt.Client("Jetson", 1883)
client.connect(MQTT_BROKER)
client.loop_start()

client.subscribe("BoundingBox")
client.subscribe("HeartRate")
client.on_message=on_message
time.sleep(1)
client.loop_stop()
