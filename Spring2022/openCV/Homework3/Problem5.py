import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 150, -1)

circle = cv.circle(blank.copy(), (200, 200), 200, 150, -1)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('First image', bitwise_xor)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Second image', bitwise_or)

cv.waitKey(0)