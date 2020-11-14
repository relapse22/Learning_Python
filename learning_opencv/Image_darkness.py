import cv2 as cv

i = cv.imread('IMAGEFILE.JPG')
i = cv.cvtColor(i, cv.COLOR_RGB2GRAY)

_, result = cv.threshold(i, 35, 255, cv.THRESH_BINARY)
# Play with the last 2 numbers to get a better result on your Image.
adaptive = cv.adaptiveThreshold(i, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4)


cv.imshow('image', i)
cv.imshow('result', result)
cv.imshow('Adaptive Result', adaptive)

cv.waitKey(0)
cv.destroyAllWindows()

