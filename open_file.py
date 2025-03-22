import cv2

## dosya okuma işlemi
image = cv2.imread('image.png')
cv2.imwrite("image_copy.jpeg", image)
