import cv2
import numpy as np
import mask
count = 0
color  = (0,0,255)
img = cv2.imread("Resources\\rubiks-cube-different-color-cubes-combination.jpg")
# cap = cv2.VideoCapture(0)

def getContour(inImg,outImg):
    contour, _ = cv2.findContours(inImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(outImg,cnt,-1,color,2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            center, radius = cv2.minEnclosingCircle(approx)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(outImg,(x,y,w,h),color,2)
            cv2.circle(outImg,(int(center[0]),int(center[1])),int(radius),color,2)


def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.createTrackbar("Thresh1", "Parameters", 150, 255,empty)
cv2.createTrackbar("Thresh2", "Parameters", 100, 255,empty)

while True:
    # a, frame = cap.read()
    frame = img.copy()
    test = frame.copy()
    blur = cv2.GaussianBlur(frame,(5,5),1)
    gray  = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    thresh1 = cv2.getTrackbarPos("Thresh1", "Parameters")
    thresh2 = cv2.getTrackbarPos("Thresh2", "Parameters")

    imgCanny = cv2.Canny(gray, thresh1, thresh2)

    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    getContour(imgDil,test)
#   create a mask of the red color

    # red = cv2.bitwise_and(frame,frame, mask=mask.rmask(hsv))
    cv2.imshow("dilate",imgDil)
    cv2.imshow("result",test)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)