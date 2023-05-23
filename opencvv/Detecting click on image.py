import cv2
import numpy as np

img = cv2.imread('resources/l1.png')

def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN :
        print(x, y )



cv2.imshow('image ', img)
cv2.setMouseCallback('image',mouse)

cv2.waitKey(0)
