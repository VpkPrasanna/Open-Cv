import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#lower_blue = np.array([110,50,50])
	#upper_blue = np.array([130,255,255])

	#lower_green = np.array([50,50,120])
	#upper_green = np.array([130,255,255])

	lower_yellow = np.array([80,100,100])
	upper_yellow = np.array([100,255,255])

	yellow_mask = cv2.inRange(hsv,lower_yellow,upper_yellow)


	#blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)
	#green_mask = cv2.inRange(hsv,lower_green,upper_green)

	#mask = blue_mask+green_mask

	res = cv2.bitwise_and(frame,frame,mask = yellow_mask)
	#res1 = cv2.bitwise_and(frame,frame,mask = green_mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',yellow_mask)
	cv2.imshow('res',res)


	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()