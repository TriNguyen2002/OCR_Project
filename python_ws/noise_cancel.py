import cv2
import numpy as np
import pytesseract

# def noise_removal(image):
#     import numpy as np
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv2.dilate(image, kernel, iterations=1)
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv2.erode(image, kernel, iterations=1)
#     image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#     image = cv2.medianBlur(image, 3)
#     return (image)

img = cv2.imread("Resources\\bt_co.jpg")
gray_im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh, im_bw = cv2.threshold(gray_im,200,255,cv2.THRESH_BINARY)
ocr_result = pytesseract.image_to_string(gray_im)
print(ocr_result)