import cv2 as cv

# Rescale the image pic1.jpg by 0.5 and display the original image and the rescaled one in separate windows.

def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


img = cv.imread('Photos/pic1.jpg')

img_rescaled = rescaleFrame(img, 0.5)

cv.imshow('Original', img)
cv.imshow('Rescaled', img_rescaled)

cv.waitKey(0)