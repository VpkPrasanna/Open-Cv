import numpy as np
import cv2

img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)

#px = img[55,55]

img[55,55]=[255,0,255]
px = img[55,55]
#print(px)

img[100:150,100:150] = [255,0,0]
#print(roi)
watch = img[37:111,107:194]
img[0:74,0:87] = watch
cv2.imshow('Image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()