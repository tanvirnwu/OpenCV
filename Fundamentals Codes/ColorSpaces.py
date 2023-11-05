import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

my_img = cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Cat', my_img)

# # Original image is in BGR format but matplotlib has no idea about it
# # Show when we display it using matplotlib it will show it in RGB format and the color looks different visually
# plt.imshow(my_img)
# plt.show()
#
# # BGR to Grayscale
# gray = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
#BGR to HSV
# hsv = cv.cvtColor(my_img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)
#
# # BGR to CieLAB
lab = cv.cvtColor(my_img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
#
# # BGR to RGB
# rgb = cv.cvtColor(my_img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)
# plt.imshow(rgb)
# plt.show()

# We cannot convert the grayscale image to HSV or LAB directly
# Frist, we have to convert it to BGR and then to HSV or LAB

# HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV to BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)


cv.waitKey(0)
