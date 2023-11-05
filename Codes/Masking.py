import cv2 as cv
import numpy as np

my_img= cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)

blank = np.zeros(my_img.shape[:2], dtype='uint8') # Dimention of the mask must be same as the image
cv.imshow('Blank Image', blank)

# mask = cv.circle(blank, (my_img.shape[1]//2, my_img.shape[0]//2+45), 100, 255, -1)
# cv.imshow('Mask', mask)
#
# masked = cv.bitwise_and(my_img, my_img, mask=mask)
# cv.imshow('Masked Image', masked)

circle = cv.circle(blank.copy(), (my_img.shape[1]//2, my_img.shape[0]//2+45), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (250, 370), 255, -1)
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked_2  = cv.bitwise_and(my_img, my_img, mask=weird_shape)
cv.imshow('Masked Image', masked_2)

cv.waitKey(0)
