import paho.mqtt.client as mqtt
import time
import sys
import io
import PIL.Image as Image

#This script subscribes to the topic passed as the first argument and saves the image that it receives, overwriting it each time a new image is received

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload))
    image = Image.open(io.BytesIO(message.payload))
    image.save('img.png')

mqttBroker ="10.38.4.212"

client = mqtt.Client("Laptop", 1883)
client.connect(mqttBroker) 

client.loop_start()

client.subscribe(sys.argv[1])
client.on_message=on_message 

time.sleep(1000)
client.loop_stop()
