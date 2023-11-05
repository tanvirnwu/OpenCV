import cv2 as cv

my_img = cv.imread('E:\\Open CV\\Images\\cat1.jpg')

cv.imshow('Cat', my_img)
cv.waitKey(0)

# Rescale Image
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

rescaleFrame()
