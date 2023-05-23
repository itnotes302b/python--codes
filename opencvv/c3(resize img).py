import cv2
img= cv2.imread('/home/pranjal/PycharmProjects/opencvv/resources/sw1.png')

cv2.imshow("image ",img)
print(img.shape) # it return 3 value height , weidth ,  number or id of channel which is BGR
imgresize = cv2.resize(img,(400,190)) #here opencv workd width*height
imgCrop = img [0:200,100:400]
cv2.imshow("Resize Image",imgresize)
cv2.imshow('Crop Image ',imgCrop)
cv2.waitKey(0)