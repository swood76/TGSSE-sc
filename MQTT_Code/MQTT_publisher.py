import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import cv2
import jetson.inference
import jetson.utils

#This script does inference on an image from a camera and publishes the bounding boxes from the detected objects via MQTT under the topic "BoundingBox"

mqttBroker ="10.38.4.25" 

client = mqtt.Client("Jetson",1883)
client.connect(mqttBroker) 


display = jetson.utils.glDisplay()
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(1280,720,"0")
while display.IsOpen():

            
            
    #display = jetson.utils.glDisplay()
   # net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
   # camera = jetson.utils.gstCamera(1280, 720, "0")
            

    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    
    display.RenderOnce(img, width, height)
    display.SetTitle("object detection | Network {:0.0f} FPS".format(net.GetNetworkFPS()))

    for detection in detections:
         client.publish("BoundingBox", str(detection))
         print(str(detection))
         #print(detections)
         #print("Just published" + str(detection) + " to topic BoundingBox")
         time.sleep(1)
