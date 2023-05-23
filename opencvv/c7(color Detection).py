# https://www.youtube.com/watch?v=WQeoO7MI0Bs 56:14
import cv2
import numpy as np
path = '/home/pranjal/PycharmProjects/opencvv/resources/sw1.png'
def empty(something):
    pass
'''
cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar',640,40)
cv2.createTrackbar('Hue Min','Trackbar',0,179,empty)
cv2.createTrackbar('Hue Max','Trackbar',179,179,empty)
cv2.createTrackbar('sat Min','Trackbar',0,255,empty)
cv2.createTrackbar('sat Max','Trackbar',255,255,empty)
cv2.createTrackbar('val Min','Trackbar',0,255,empty)
cv2.createTrackbar('val Max','Trackbar',255,255,empty)'''


cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar',640,40)
cv2.createTrackbar('Hue Min','Trackbar',0,179,empty)
cv2.createTrackbar('Hue Max','Trackbar',179,179,empty)
cv2.createTrackbar('sat Min','Trackbar',0,255,empty)
cv2.createTrackbar('sat Max','Trackbar',204,255,empty)
cv2.createTrackbar('val Min','Trackbar',142,255,empty)
cv2.createTrackbar('val Max','Trackbar',255,255,empty)

while True :
    img = cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min','Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max','Trackbar')
    s_min = cv2.getTrackbarPos('sat Min','Trackbar')
    s_max = cv2.getTrackbarPos('sat Max','Trackbar')
    v_min = cv2.getTrackbarPos('val Min','Trackbar')
    v_max = cv2.getTrackbarPos('val Max','Trackbar')
    print(h_max,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgresult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Image",img)
    cv2.imshow('Image HSV', imgHSV)
    cv2.imshow('Mask',mask)
    cv2.imshow('Image Result',imgresult)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()