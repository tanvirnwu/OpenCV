import cv2 as cv
import numpy as np

my_img= cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)

gray = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Sinple Thresholding
# cv.threshold(image, threshold value, max value, threshold type)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# cv.threshold(image, threshold value, max value, threshold type)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
# cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# Here 11 means that the neighbourhood area is 11x11 pixels.
# Here 3 means that the constant C is 3.
# constant C is just a constant that is subtracted from the mean or weighted mean calculated.
# Subtracting by a constant C helps to fine tune the thresholding.
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)
