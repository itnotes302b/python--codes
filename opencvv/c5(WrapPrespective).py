import cv2
import numpy as np
width,height = 250,300
img=cv2.imread('/home/pranjal/PycharmProjects/opencvv/resources/l1.png')
pts1 = np.float32([[89.0,90.5],[164.5,74.0],[114.0,162.0],[189.0,140.5]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgopt = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
# cv2.waitKey(10000)
cv2.imshow("Image",imgopt)

cv2.waitKey(0)