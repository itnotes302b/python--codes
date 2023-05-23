import cv2
import numpy as np


framewidth = 650
frameheight= 480
cap = cv2.VideoCapture(0, cv2.CAP_V4L) # 0 uses bydefault webcam having id no 0
cap.set(3,framewidth)# setting width of webcam id = 3
cap.set(4,frameheight)# setting height is = 4
cap.set(10,150)# 10 means id =10 for increasing brightness 150 means how

while True:
    sucess,img = cap.read()
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break