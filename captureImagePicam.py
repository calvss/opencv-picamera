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
        image = image[::-1]
        
        q.put(image)
        rawCapture.truncate(0)
        
        print("FPS: ", 1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop
        
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Frame", gray)
        #key = cv2.waitKey(1) & 0xFF
        
        #rawCapture.truncate(0)
        
        #if key == ord("q"):
        #    break

    camera.close()
