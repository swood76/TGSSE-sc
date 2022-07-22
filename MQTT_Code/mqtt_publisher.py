#!/usr/bin/env python
'''
This script does inference on an image from a camera and publishes the bounding boxes
from the detected objects via MQTT under the topic "BoundingBox"
'''
import time
import jetson.inference
import jetson.utils
import paho.mqtt.client as mqtt
import addr_info

client = mqtt.Client("Jetson",1883)
client.connect(addr_info.MOSQUITTO_IP)

display = jetson.utils.glDisplay()
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(1280,720,"0")
while display.IsOpen():
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    #display.SetTitle("object detection | Network {:0.0f} FPS".format(net.GetNetworkFPS()))
    display.SetTitle(f"object detection | Network {net.GetNetworkFPS()} FPS")
    for detection in detections:
        client.publish("BoundingBox", str(detection))
        print(str(detection))
        #print(detections)
        #print("Just published" + str(detection) + " to topic BoundingBox")
        time.sleep(1)
