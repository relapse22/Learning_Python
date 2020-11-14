import cv2 as cv

# To use your own webcam range form 0 to so on.
# video = cv.VideoCapture(0)

# To use a video (.mp4, .mov)
video = cv.VideoCapture('spin.mp4')
# Play with the numbers to get a better quality in the video.
subtractor = cv.createBackgroundSubtractorMOG2(200, 50)

while True:

    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('White&Black', mask)

        if cv.waitKey(5) == ord('X'):
            break

    else:
        video = cv.VideoCapture('spin.mp4')

cv.destroyAllWindows()
video.release()