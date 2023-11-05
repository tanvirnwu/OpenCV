import cv2 as cv
import numpy as np

my_img = cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)

blank = np.zeros(my_img.shape, dtype='uint8')
cv.imshow('Blank Image', blank)

# Convert to Gray Scale
my_gray_img = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat Image', my_gray_img)

# Method One for Contours detections
'''
my_blur_img = cv.GaussianBlur(my_gray_img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur Cat Image', my_blur_img)

canney = cv.Canny(my_blur_img, 125, 175)
cv.imshow('Canny Edges', canney)

contours, hierarchies = cv.findContours(canney, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(my_blur_img, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', my_blur_img)
'''

# Method Two for Contours detections
ret, thresh = cv.threshold(my_gray_img, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
