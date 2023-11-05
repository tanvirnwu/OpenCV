import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle) # It will show the intersection
cv.imshow('Bitwise AND', bitwise_and) # Returns the bitwise conjunction of two arrays

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle) # It will show the union
cv.imshow('Bitwise OR', bitwise_or) # Returns the bitwise 'inclusive or' of two arrays

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle) # It will show the intersection
cv.imshow('Bitwise XOR', bitwise_xor) # Returns the bitwise 'exclusive or' of two arrays

# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle) # It will invert the color
cv.imshow('Bitwise NOT', bitwise_not) # Returns the bitwise inversion of the input array elements.

cv.waitKey(0)
