import numpy as np
import cv2
import pytesseract

def rescale(frame, scale =1.0):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)
    dim = (w,h)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    #print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    # print(angle)
    if angle < -45:
        angle = 90 + angle
    return -1.0 * (90-angle)
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center,angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

image = rescale(cv2.imread("Resources\\toy_alphabet.jpg"),0.5)
# image = cv2.GaussianBlur(image,(3,3),0)



angle = getSkewAngle(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("result.png",rescale(rotateImage(image,angle),1))
kernel = np.ones((1, 1), np.uint8)

result= cv2.imread("result.png")
rotated = result.copy()
rotated = cv2.GaussianBlur(rotated,(3,3),0)
rotated = cv2.dilate(rotated,kernel,iterations=1)
_,rotated = cv2.threshold(rotated,195,255,cv2.THRESH_BINARY)
rotated = cv2.erode(rotated,kernel,iterations=1)

# rotated = cv2.morphologyEx(rotated, cv2.MORPH_DILATE, kernel)

# _, threshold = cv2.threshold(rotated,200,255,cv2.THRESH_BINARY)

cv2.imshow("before",image)
cv2.imshow("after", rotated)
text = pytesseract.image_to_string(rotated)
print(text)
cv2.waitKey(0)