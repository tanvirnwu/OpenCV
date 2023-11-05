import cv2 as cv
import numpy as np

my_img= cv.imread('E:\\Open CV\\Images\\cat2.jpg')
cv.imshow('Original Cat Image', my_img)

gray = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# Laplacian is a derivative of an image
lap = cv.Laplacian(gray, cv.CV_64F) # cv.CV_64F is the data type
lap = np.uint8(np.absolute(lap)) # Convert the data type to uint8
cv.imshow('Laplacian', lap)

# Sobel
# Sobel is a combination of Gaussian Blur and Laplacian
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # cv.CV_64F is the data type
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # cv.CV_64F is the data type
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)


# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)



cv.waitKey(0)
