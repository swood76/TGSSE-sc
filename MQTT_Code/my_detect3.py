#!/usr/bin/env python
'''
This actively runs inference on a video stream from a connected camera
'''
import jetson.inference
import jetson.utils

display = jetson.utils.glDisplay()
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource(r"/dev/video0")

while display.IsOpen():
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    #display.SetTitle("object detection | Network {:0.0f} FPS".format(net.GetNetworkFPS()))
    display.SetTitle(f"object detection | Network {net.GetNetworkFPS()} FPS")
