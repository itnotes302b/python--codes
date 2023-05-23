# chapter 2 BAsic Functions
import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8)

img=cv2.imread('/home/pranjal/PycharmProjects/opencvv/resources/sw1.png',1)
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblr = cv2.GaussianBlur(img,(7,7),0) #(7,7)abount of blr scale we want it should always be odd number next is sigman x which we have is 0
imgCanny = cv2.Canny(img,100,100)#Canny gives edges 100,100 is a threshold values u van change adjust threshhold values
# Now if the edges are not connected properly We can adjust using Dilation
imgDilation = cv2.dilate(imgCanny ,kernal,iterations=1)
imgErode = cv2.erode(imgDilation,kernal,iterations=1)
cv2.imshow("Gray Image",imggray)
cv2.imshow("Blr Image",imgblr)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("Erod Image",imgErode)
cv2.waitKey(10000)