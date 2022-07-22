#!/usr/bin/env python
'''
This script subscribes to the topic passed as the first argument
and saves the image that it receives, overwriting it each time a new image is received
'''
import time
import sys
import io
import paho.mqtt.client as mqtt
from PIL import Image
import addr_info

def on_message(client, userdata, message):
    '''This method handles the messages that are received'''
    print("received message: " ,str(message.payload))
    image = Image.open(io.BytesIO(message.payload))
    image.save('img.png')

client = mqtt.Client("Laptop", 1883)
client.connect(addr_info.MOSQUITTO_IP)

client.loop_start()

client.subscribe(sys.argv[1])
client.on_message=on_message

time.sleep(1000)
client.loop_stop()
