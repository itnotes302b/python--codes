import cv2
import numpy as np



# This is a special function to arrange image in stack
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getcontrous(img):
    controus , hierchacy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in controus :
        area = cv2.contourArea(cnt)
        print(area)
        # if area > 500 : to reduce noise
        cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
        perimeter= cv2.arcLength(cnt,True)
        print(perimeter)
        approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
        print(len(approx))
        objcorner = len(approx)
        x,y,w,h = cv2.boundingRect(approx)

        if objcorner == 3 : objecttype ='Triangle'

        elif objcorner == 4 :
            aspRatio= w/float(h)
            if aspRatio >0.95 and aspRatio < 1.05 :
                objecttype = 'Square'
            else: objecttype = 'rectangle'



        elif objcorner == 5 :objecttype = 'pentagone'

        elif objcorner == 6 :objecttype = 'Hexagone'

        elif objcorner > 4: objecttype = 'circle'

        else: objecttype='None'
        cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,0,123),2)
        cv2.putText(imgcontour,objecttype,((x+(h//2),y+(w//2))),cv2.FONT_ITALIC,0.5,
                    (0,0,125),2)




img = cv2.imread('resources/shape.jpg')
imgcontour = img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgcanny =  cv2.Canny(imgBlur,50,50)

getcontrous(imgcanny)

imgBlank = np.zeros_like(img)
imgstack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgcanny,imgcontour,imgBlank]))


cv2.imshow("Stack Image",imgstack)

# cv2.imshow('Image',img)
# cv2.imshow('Image Gray',imgGray)
# cv2.imshow('Image Blur',imgBlur)


cv2.waitKey(0)