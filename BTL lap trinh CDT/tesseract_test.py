import cv2
import numpy as np
import pytesseract

img = cv2.imread("Resources\\textselection-example.png")


hImg, wImg,_ =img.shape
boxes = pytesseract.image_to_boxes(img)
for i in boxes.splitlines():
    # print(i)
    i = i.split(' ')
    # print(i)
    x,y,w,h = int(i[1]), int(i[2]),int(i[3]),int(i[4])


cv2.imshow("1",img)
cv2.waitKey(0)