import cv2
import numpy as np

# img = cv2.imread('resources/l1.png')

width,height = 250,300
img=cv2.imread('/home/pranjal/PycharmProjects/opencvv/resources/l1.png')
pts1 = np.float32([[89.0,90.5],[164.5,74.0],[114.0,162.0],[189.0,140.5]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgopt = cv2.warpPerspective(img,matrix,(width,height))

for x in range (0,4):

    cv2.circle(img,(pts1[X][0],pts1[x],[1]),15,(0,225,0),cv2.FILLED)

cv2.imshow("Image",img)

cv2.imshow("Image",imgopt)


cv2.waitKey(0)
