import cv2 as cv

#Draw an orange rectangle with thickness 2 on the image pic2.jpg. Use appropriate measures for the rectangle
# so that the whole rectangle is visible. Display the original image and the changed one in separate windows.

img = cv.imread('Photos/pic2.jpg')
cv.imshow('Original', img)

height, width = img.shape[0:2]
center = (height//2, width//2)
point2 = (height//4, width//4)
cv.rectangle(img, center, point2, (0, 128, 255), thickness=2)

cv.imshow('Rectangle', img)

cv.waitKey(0)