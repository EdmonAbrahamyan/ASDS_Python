import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Repeat the previous exercise without converting the image to grayscale and get 3 histograms
# for each of the color channels on one plot.

img = cv.imread('Photos/pic1.jpg')
colors = ('b', 'g', 'r')

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('img')
plt.show()

for i, col in enumerate(colors):
    print(i)
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
plt.show()
