import numpy as np

import cv2 as cv

my_img = cv.imread('E:\\Open CV\\Images\\cat1.jpg')
cv.imshow('original Cat Image', my_img)

# Translation
def translate(img, x, y):
    translate = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translate, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(my_img, 100, 100)
# cv.imshow('Translated', translated)

translated = translate(my_img, -100, -100)
# cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(my_img, -45)
# cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
# cv.imshow('Rotated_rotated', rotated_rotated)

# Resizing
resized = cv.resize(my_img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Flipping
# Flip code can be 0, 1 or -1
# o means flipping vertically,
# 1 means flipping horizontally
# and -1 means flipping both vertically and horizontally
flip = cv.flip(my_img, -1)
# cv.imshow('Flip', flip)

# Cropping
cropped = my_img[200:500, 300:500]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
