import cv2 as cv
import numpy as np

# Draw a red filled circle in the middle of the image pic2.jpg. Use an appropriate radius value so
# that the whole circle is visible. Display the original image and the changed one in separate
# windows.

img = cv.imread('Photos/pic2.jpg')

cv.imshow('Original', img)
height, width = img.shape[0:2]
center = (height//2, width//2)
cv.circle(img, center, 50, (0, 0, 255), thickness=-1)
cv.imshow('Circle', img)
cv.waitKey(0)