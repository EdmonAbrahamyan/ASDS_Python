import cv2 as cv
import numpy as np
# Open the image pic2.jpg and display it with the name pic2. Convert the image to grayscale. Try
# detecting the edges with a method of your choice. Use one technique of your choice on the
# image from what we have learned so far and try to get a better result. (better than simply using
# some edge detection technique on a grayscale of a raw image)

img = cv.imread('Photos/pic2.jpg')
cv.imshow('pic2', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)