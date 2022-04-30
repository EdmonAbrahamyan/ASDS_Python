import cv2 as cv

# Open the image pic2.jpg and display it with the name pic2. Resize the image to have 2 times
# bigger width and the same height as the original image, use INTER_AREA interpolation. Then
# resize the original image to have 2 times smaller height and the same width as the original image,
# use INTER_CUBIC interpolation. Display both versions in separate windows.

img = cv.imread('Photos/pic2.jpg')
cv.imshow('pic2', img)

height, width = img.shape[0], img.shape[1]
resize = cv.resize(img, (width * 2, height), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resize)

cv.waitKey(0)