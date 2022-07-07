import cv2
import jetson.inference
import jetson.utils

display = jetsn.utils.glDisplay()
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")Pe

while display.IsOpen():
        img, width, height = camera.CaptureRGBA()
            detections = net.Detect(img, width, height)
                display.RenderOnce(img, width, height)
                    display.SetTitle("object detection | Network {:0.0f} FPS".format(net.GetNetworkFPS()))

