import cv2 as cv

# Open the image pic2.jpg and display it with the name pic2. Try to detect the image edges using
# Canny edge detector and display the result in a separate window. Then run the edge detector
# on a blurred version of an image (use a window size of your choice) and display the result in a
# different window to compare.

img = cv.imread('Photos/pic2.jpg')
cv.imshow('pic2', img)

canny = cv.Canny(img, 125, 157)
cv.imshow('canny', canny)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 157)
cv.imshow('blurred canny', canny)

cv.waitKey(0)