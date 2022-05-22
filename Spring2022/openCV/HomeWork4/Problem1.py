import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and
# plot the histogram of pixel intensities using matplotlib.

img = cv.imread('Photos/pic1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
gray_hist = [i[0] for i in gray_hist]

x = np.arange(256)
plt.plot(x, gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

