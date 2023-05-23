import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:] = 255,0,0 #to select Blue
cv2.line(img,(100,0),(300,300),(0,255,0),3)
#to selectimage  (startingpoint),(ending Point),(color this will give greay),thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# img.shape[1] = width,img.shape[0]= height cv2 works width*height
cv2.rectangle(img,(20,200),(400,500),(0,0,227),2)
# cv2.rectangle(img,(20,200),(400,500),(0,0,227),cv2.FILLED)
cv2.circle(img,(100,200),10,(129,0,117),2)
cv2.putText(img,'OpenCV',(350,200),cv2.FONT_ITALIC,1,(113,243,0),2)

cv2.imshow("Image",img)

cv2.waitKey(0)