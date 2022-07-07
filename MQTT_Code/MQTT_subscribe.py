import paho.mqtt
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
        print("received message: " ,str(message.payload.decode("utf-8")))


mqttBroker ="150.250.106.147"

client = mqtt.Client("Jetson", 1883)
client.connect(mqttBroker) 
client.loop_start()

client.subscribe("BoundingBox")
client.subscribe("HeartRate")
client.on_message=on_message 
time.sleep(1)
client.loop_stop()
