import cv2

img = cv2.imread('assets/linux_logo.jpg', -1)
img = cv2.resize(img, (200,200))

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()