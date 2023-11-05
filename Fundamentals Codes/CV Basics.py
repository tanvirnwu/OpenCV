import cv2 as cv

my_img=cv.imread('E:\\Open CV\\Images\\cat1.jpg')
cv.imshow('Original Cat Image',my_img)

# Converting to grayscale
gray = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Bluring an Image
# Here 7 by 7 is the kernel size
my_blur_img = cv.GaussianBlur(my_img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', my_blur_img)

# Edge Cascade
# canny = cv.Canny(my_img, 125, 175) # More edges as the image is clear
canny = cv.Canny(my_blur_img, 125, 175) # Edges are reduced as the image is blurred
# cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (6,6), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (6,6), iterations=3)
# cv.imshow('Eroded', eroded)


# Resizing to 500 by 500, ignoring the aspect ratio
resized = cv.resize(my_img, (350,450), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized Image', resized)

# Resize by to 500 by 500, keeping the aspect ratio
resized = cv.resize(my_img, (0,0), fx=0.5, fy=0.5)
# cv.imshow('Resized Image', resized)

# Cropping the image
cropped = my_img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)

