import cv2 as cv

# Rescale Frame Function
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Resolution Change Function
def changeRes(width, height):
    # Live Videos #Not going to work with saved videos
    capture.set(3, width)
    capture.set(4, height)


# Rescale Videos
capture = cv.VideoCapture('E:\\Open CV\\Videos\\dog2.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Resize Images
my_img = cv.imread('E:\\Open CV\\Images\\cat1_large.jpg')
cv.imshow('Cat', my_img)
my_resized_img = rescaleFrame(my_img, scale=0.3)
cv.imshow('Cat Resized', my_resized_img)
cv.waitKey(0)


