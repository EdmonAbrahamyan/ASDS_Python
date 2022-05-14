import cv2 as cv

# Open the image pic1.jpg and display it with the name pic1. Separate the image into its 3
# channels. Display both the colored and grayscale versions of each channel in separate windows.

img = cv.imread('Photos/pic1.jpg')
cv.imshow('pic1', img)

blue, green, red = cv.split(img)

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)



cv.waitKey(0)