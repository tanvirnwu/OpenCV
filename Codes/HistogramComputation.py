import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

my_img= cv.imread('E:\\Open CV\\Images\\cat1.jpg')
cv.imshow('Original Cat Image', my_img)


# #Gray Scale Histogram
# blank = np.zeros(my_img.shape[:2], dtype='uint8') # Dimention of the mask must be same as the image
# gray = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# circle = cv.circle(blank.copy(), (my_img.shape[1]//3, my_img.shape[0]//3), 100, 255, -1)
# mask = cv.bitwise_and(gray, gray, mask = circle)
# cv.imshow('Mask', mask)


#Gray Scale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
#
# plt.figure()
# plt.title('Gray Scale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()



# Color Histogram
blank = np.zeros(my_img.shape[:2], dtype='uint8') # Dimention of the mask must be same as the image
mask = cv.circle(blank.copy(), (my_img.shape[1]//2, my_img.shape[0]//2), 200, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(my_img, my_img, mask = mask)
cv.imshow('Masked Image', masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([my_img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()




cv.waitKey(0)
