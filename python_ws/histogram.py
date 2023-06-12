
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# rescale funct
def rescale(frame, scale = 0.3):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)
    dim = (w,h)
    return cv.resize(img, dim, interpolation=cv.INTER_AREA)


img = cv.imread('Resources\murakami_book.jpg')
resize = rescale(img)
cv.imshow('book', resize)

# masking
blank = np.zeros(resize.shape[:2], dtype='uint8')

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (resize.shape[1]//2,resize.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(resize,resize,mask=mask)
# thresh
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)
# GRayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
# plt.show()


# Colour Histogram


cv.waitKey(0)