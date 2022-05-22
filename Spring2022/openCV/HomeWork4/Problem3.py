import cv2 as cv
import matplotlib.pyplot as plt

# Open the image pic1.jpg and display it with the name pic1. Binarize the image using 3 different
# methods: choosing the threshold by hand and using THRESH_BINARY method, using adaptive
# thresholding with mean and gaussian methods. Display the 3 results in separate windows

img = cv.imread('Photos/pic1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
th3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding' ]
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

