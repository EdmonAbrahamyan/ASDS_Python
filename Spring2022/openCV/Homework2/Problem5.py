import cv2 as cv
import numpy as np

# Open the image pic2.jpg and display it with the name pic2. Translate the image to go down by
# 200 pixels and to the right by 50 pixels. Then rotate the image around its center by 50 degrees.
# Then flip the resulting image both vertically and horizontally. Display the result after each action
# in a separate window.

img = cv.imread('Photos/pic2.jpg')
cv.imshow('pic2', img)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimentions)


def rotate(img, angle, rotPoint=None):
    height, width = (img.shape[0], img.shape[1])

    if rotPoint == None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)


translated = translate(img, 200, 50)
cv.imshow('Translated', translated)

rotated = rotate(translated, 50)
cv.imshow('Rotated', rotated)

flip = cv.flip(rotated, -1)

cv.imshow('flipped', flip)

cv.waitKey(0)
