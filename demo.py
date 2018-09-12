import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('index.jpeg',-1)
#Showing images uisng OpenCV
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Show Images using Matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.imshow(img,cmap='gray',interpolation='kaiser')
plt.show()

#Save the image to the disk using opencv
cv2.imwrite('demo.jpg',img)
