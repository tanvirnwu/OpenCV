import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain color
blank[200:300, 300:400] = 60, 255, 20
cv.imshow('Green', blank)

# Draw a Rectangle
cv.rectangle(blank, (10, 50), (150, 250), (125, 100, 150), thickness=-1)
cv.imshow('Rectangle', blank)


cv.rectangle(blank, (10, 50), (150, 250), (125, 100, 150), thickness=-1)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (10, 50), (blank.shape[1]//2, blank.shape[0]//3), (125, 100, 150), thickness=-1)
cv.imshow('Rectangle', blank)

# Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a Line
cv.line(blank, (100, 350), (300, 400), (255, 255, 255), thickness=5)
cv.imshow('Line', blank)

# Write Text
cv.putText(blank, 'Hello, my name is Tanvir.', (50, 450), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (150, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
# my_img = cv.imread('E:\\Open CV\\Images\\cat1.jpg')
# cv.imshow('Cat', my_img)
