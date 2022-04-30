import cv2 as cv

# Open the image pic3.jpg and display it with the name pic3. Find the edges of the image using
# Canny edge detector and then try to find its contours with parameters of your choice. Then
# convert the original image to grayscale and try to find the contours on a blurred version of the
# grayscale of the original image. Display the 2 results in separate windows to compare.

img = cv.imread('Photos/pic3.jpg')
cv.imshow('pic3', img)

canny = cv.Canny(img, 125, 140)
cv.imshow('Canny', canny)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

blur = cv.GaussianBlur(gray_img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 140)
cv.imshow('Blurred Gray Canny', canny)

cv.waitKey(0)