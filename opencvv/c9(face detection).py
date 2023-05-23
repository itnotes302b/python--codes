import cv2
import numpy as np

facecascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

img = cv2.imread('resources/Linus.jpg')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = facecascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,234),2)


cv2.imshow('Result',img)
cv2.waitKey(0)


