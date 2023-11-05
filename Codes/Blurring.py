import cv2 as cv
import numpy as np

my_img= cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)

# Average Blur
average = cv.blur(my_img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(my_img, (7, 7), 0)  # 0 is the standard deviation
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(my_img, 7)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(my_img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)


