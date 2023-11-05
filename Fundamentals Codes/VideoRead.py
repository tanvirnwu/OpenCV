import cv2 as cv

capture = cv.VideoCapture('E:\\Open CV\\Videos\\dog1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyWindow()

