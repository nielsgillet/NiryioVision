# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
	
	
    blurred_image=cv2.GaussianBlur(image,(5,5),0)
    hsv=cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB)

    lower_red=np.array([0,0,0])
    upper_red=np.array([170,80,80])
    mask=cv2.inRange(hsv,lower_red,upper_red)

    _, contours, _=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area=cv2.contourArea(contour)
        approx=cv2.approxPolyDP(contour,0.02*cv2.arcLength(contour,True),True)
        if area >2000:
            cv2.drawContours(image,contours,-1,(0,255,0),3)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            if len (approx) == 12:
                cv2.putText(image, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len (approx) ==4:
                cv2.putText(image, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len (approx) ==3:
                cv2.putText(image, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            elif len (approx) == 8:
                cv2.putText(image, "Round", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    cv2.imshow("frame",image)
    cv2.imshow("mask",mask)
    key = cv2.waitKey(1) & 0xFF

 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    if key == ord("q"):
	    break
