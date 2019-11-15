# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
 

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (0, 0, 0)
greenUpper = (179, 255, 255)
pts = deque(maxlen=64)
 
#grab the reference to the webcam
vs = VideoStream(src=0).start()
 
 
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
    frame = vs.read()



    # if you don't get a frame.  we can't continue
    if frame is None:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
    

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask

    # find contours in the mask and initialize the current
    # (x, y) center of the ball

    # only proceed if at least one contour was found


    # update the points queue

    # loop over the set of tracked points

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

vs.stop()
 
# close all windows
cv2.destroyAllWindows()