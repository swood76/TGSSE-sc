import paho.mqtt.client as mqtt
import time
import sys
import io
import PIL.Image as Image

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload))
    image = Image.open(io.BytesIO(message.payload))
    image.save('img.png')

mqttBroker ="150.250.106.147"

client = mqtt.Client("Laptop", 1883)
client.connect(mqttBroker) 

client.loop_start()

client.subscribe(sys.argv[1])
client.on_message=on_message 

time.sleep(30)
client.loop_stop()
