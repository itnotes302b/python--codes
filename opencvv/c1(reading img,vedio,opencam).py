import cv2
import numpy
# Image
# '''
img = cv2.imread('resources/sw1.png')
cv2.imshow('output',img)
cv2.waitKey(1000)#waitkey means for how many milisec outlput has to wait
# '''
# Vedio
'''
cap = cv2.VideoCapture('/home/pranjal/PycharmProjects/opencvv/resources/s2.webm')

while True :
    sucess , image= cap.read()
    cv2.imshow('vedio',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
# Web Cam
'''
cap = cv2.VideoCapture(0, cv2.CAP_V4L) # 0 uses bydefault webcam having id no 0
cap.set(3,650)# setting width of webcam id = 3
cap.set(4,480)# setting height is = 4
cap.set(10,100)# 10 means id =10 for increasing brightness
while True :
    sucess , img= cap.read()
    cv2.imshow('vedio',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

'''

# cv2.destroyAllWindows()