import cv2
import time

from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

def captureImagePicam(q):

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr"):
        start_time = time.time()
        image = frame.array
        
        q.put(frame)
        
        print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop

    camera.close()
