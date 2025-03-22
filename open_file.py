import cv2

## dosya okuma işlemi

# imread -> dosya okuma işlemi yapar
# imwrite -> dosya yazma işlemi yapar


image = cv2.imread('image.png')
cv2.imwrite("image_copy.jpeg", image)
