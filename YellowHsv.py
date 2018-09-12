import cv2
import numpy as np
yellow = np.uint8([[[0,0,255]]])
yellow_hsv = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
print(yellow_hsv)