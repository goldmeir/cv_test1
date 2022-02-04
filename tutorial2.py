import cv2
import random

def showtime(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('assets/linux_logo.jpg', -1)
# print(img.shape)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255) for i in range(3)]

showtime(img)