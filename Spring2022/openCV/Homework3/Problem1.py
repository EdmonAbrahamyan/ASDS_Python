import cv2 as cv

# Open the image pic1.jpg and display it with the name pic1. Convert the image to the following
# formats and display in separate windows: RGB, HSV, LAB, grayscale

img = cv.imread('Photos/pic1.jpg')
cv.imshow('pic1', img)

img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', img_RGB)

img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', img_HSV)

img_LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', img_LAB)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

cv.waitKey(0)