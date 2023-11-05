import cv2 as cv
import numpy as np

my_img= cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)


b,g,r = cv.split(my_img)

cv.imshow('Blue Channel', b) # Blue color will be shown
cv.imshow('Green Channel', g) # Green color will be shown
cv.imshow('Red Channel', r) # Red color will be shown

print(my_img.shape) # The shape of the image will be 3D
print(b.shape) # The shape of the image will be 2D
print(g.shape) # The shape of the image will be 2D
print(r.shape) # The shape of the image will be 2D

# Merge the color channels
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

# Merge the color channels with a blank image
blank = np.zeros(my_img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank]) # Blue color will be shown
green = cv.merge([blank, g, blank]) # Green color will be shown
red = cv.merge([blank, blank, r]) # Red color will be shown


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(blue.shape) # The shape of the image will be 3D
print(green.shape) # The shape of the image will be 3D
print(red.shape) # The shape of the image will be 3D

cv.waitKey(0)
