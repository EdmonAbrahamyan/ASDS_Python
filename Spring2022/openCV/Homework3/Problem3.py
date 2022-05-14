import cv2 as cv

# Open the image pic2.jpg and display it with the name pic2. Blur the picture using average and
# bilateral blurring methods and display in separate windows. (For the parameters, use the values
# of your choice). Write a short comment if you see any particular difference when using different
# parameter values for the second method and comparing it to the averaging method.

img = cv.imread('Photos/pic2.jpg')
cv.imshow('pic2', img)

average = cv.blur(img, (7, 7))
cv.imshow('average blur', average)

bilateral = cv.bilateralFilter(img, 5, 10, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)