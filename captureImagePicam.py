import cv2
import time

from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

def captureImage():

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)

    start_time = time.time()

    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array
    frame = frame[::-1]

    camera.close()

    print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop
    return frame
