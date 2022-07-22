#!/usr/bin/env python
'''
This script subscribes to both the HeartRate and BoundingBox
topics and prints the data it receives to the terminal
'''
import sys
import time
import paho.mqtt.client as mqtt
import addr_info

def on_message(client, userdata, message):
    '''
    Decodes the received text and prints it to the console
    '''
    print("received message: " ,str(message.payload.decode("utf-8")))

client = mqtt.Client("jetson", 1883)
client.connect(addr_info.MOSQUITTO_IP)
client.loop_start()

client.subscribe("BoundingBox")
client.subscribe("HeartRate")
client.on_message=on_message
time.sleep(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
client.loop_stop()
