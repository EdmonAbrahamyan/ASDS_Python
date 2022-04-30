import cv2 as cv

# Open the image pic1.jpg and display it with the name pic1. Blur the image using Gaussian blur
# using 2 different windows sizes: (3, 3) and (11, 11) and display both versions in separate
# windows to compare with the original image.

img = cv.imread('Photos/pic1.jpg')
cv.imshow('pic1', img)

blur3 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blur3', blur3)

blur11 = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('blur11', blur11)

cv.waitKey(0)