#!/usr/bin/env python
'''
Runs inference on the video feed that an
attached camera takes
'''
import jetson.inference
import jetson.utils

display = jetson.utils.glDisplay()
net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
#:camera = jetson.utils.videoSource("/dev/video0")
#print(camera)
camera = jetson.utils.gstCamera(1280, 720, "0")
#display = jetson.utils.videoOutput("rtp://150.250.220.170")
#camera = jetson.utils.videoSource("/dev/video0")
#display = jetson.utils.videoOutput("rtp://169.254.190.201")
#net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
while display.IsOpen():
    img, width,height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    #display.SetTitle("object detection | Network {:0.0f} FPS".format(net.GetNetworkFPS()))
    display.SetTitle(f"Object detection | Network {net.GetNetworkFPS()} FPS")
