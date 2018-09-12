import cv2
import numpy as np

img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
#line Parameters (image,starting point,ending point,color,width of the line)
cv2.line(img,(0,0),(150,150),(0,0,0),15)

cv2.rectangle(img,(15,25),(200,150),(0,255,255),5)
#CIrcle Parameters (imageFile,starting point,radius,widthofthe circle)
cv2.circle(img,(300,50),30,(0,255,0),-1)

pts = np.array([[50,5],[70,30],[90,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,0,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'VPK!',(15,99),font,1,(200,255,255),5,cv2.LINE_AA)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWIndows()