import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
img2 = np.zeros((512, 512, 3), np.uint8)
img3 = np.zeros((512, 512, 3), np.uint8)
img4 = np.zeros((512, 512, 3), np.uint8)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img2,(447,63), 63, (0,0,255), -1)
cv.ellipse(img3,(256,256),(100,50),0,0,180,255,-1)
cv.line(img4, (0, 0), (511, 511), (255, 0, 0), 5)

font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img,'Hilmi',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)


cv.imwrite('line.jpg', img)
cv.imshow('image', img)

cv.imwrite('circle.jpg', img2)
cv.imshow('image', img2)

cv.imwrite('ellipse.jpg', img3)
cv.imshow('image', img3)

cv.imwrite('rectangle.jpg', img4)
cv.imshow('image', img4)
