import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(0)

cv2.namedWindow('image')

def callback(x):
    pass

ilowH = 0
ihighH = 179
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

cv2.createTrackbar('lowH', 'image', ilowH, 179, callback)
cv2.createTrackbar('highH', 'image', ihighH, 179, callback)

cv2.createTrackbar('lowS', 'image', ilowS, 255, callback)
cv2.createTrackbar('highS', 'image', ihighS, 255, callback)

cv2.createTrackbar('lowV', 'image', ilowV, 255, callback)
cv2.createTrackbar('highV', 'image', ihighV, 255, callback)

while(True):
	_, frame = cap.read()

	frame = imutils.resize(frame, width=600)

	ilowH = cv2.getTrackbarPos('lowH', 'image')
	ihighH = cv2.getTrackbarPos('highH', 'image')
	ilowS = cv2.getTrackbarPos('lowS', 'image')
	ihighS = cv2.getTrackbarPos('highS', 'image')
	ilowV = cv2.getTrackbarPos('lowV', 'image')
	ihighV = cv2.getTrackbarPos('highV', 'image')

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_hsv = np.array([ilowH, ilowS, ilowV])
	higher_hsv = np.array([ihighH, ihighS, ihighV])
	mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
	
	cv2.imshow("thresh", mask)
	cv2.imshow("image", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
     
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
	
