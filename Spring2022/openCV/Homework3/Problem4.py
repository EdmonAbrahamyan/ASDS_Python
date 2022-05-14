import cv2 as cv
import numpy as np

img = cv.imread('Photos/pic2.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)

masked_image = cv.bitwise_and(img, img, mask=mask)

cv.imshow('original image', img)
cv.imshow('masked with circle', masked_image)

cv.waitKey(0)
