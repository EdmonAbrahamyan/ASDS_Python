import cv2 as cv

# Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and
# display in a separate window to compare with the original image.

img = cv.imread('Photos/pic1.jpg')
cv.imshow('Original', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

cv.waitKey(0)