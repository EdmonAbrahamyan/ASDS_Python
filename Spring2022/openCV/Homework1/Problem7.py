from _socket import herror

import cv2 as cv

# Draw a line starting from the left lower corner and ending in the right upper corner of the image
# pic1.jpg. Display the original image and the changed one in separate windows.

img = cv.imread('Photos/pic1.jpg')
cv.imshow('Original', img)

height, width = img.shape[0:2]

cv.line(img, (0, height), (width, 0), (0, 0, 120), thickness=3)

cv.imshow('With line', img)

cv.waitKey(0)
