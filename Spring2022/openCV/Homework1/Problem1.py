import cv2 as cv
# Open images pic1.jpg, pic2.jpg and pic3.jpg and display in separate windows with the names pic1, pic2 and pic3 correspondingly.

img1 = cv.imread('Photos/pic1.jpg')
img2 = cv.imread('Photos/pic2.jpg')
img3 = cv.imread('Photos/pic3.jpg')

cv.imshow('Pic1', img1)
cv.imshow('Pic2', img2)
cv.imshow('Pic3', img3)

cv.waitKey(0)