import cv2
import numpy as np

def rescale(frame, scale = 0.2):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)
    dim = (w,h)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

# Load an image
image = cv2.imread("Resources\murakami_book.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(rescale(image,0.3), cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_image,(3,3),0)

def threshold_callback(value):
    # Apply the threshold on the image
    _, thresholded = cv2.threshold(gray_image, value, 255, cv2.THRESH_BINARY)

    # Display the thresholded image
    cv2.imshow("Thresholded Image", thresholded)

# Create a window for the image and trackbar
cv2.namedWindow("Thresholded Image")
cv2.createTrackbar("Threshold", "Thresholded Image", 0, 255, threshold_callback)

while True:
    # Get the current threshold value
    threshold_value = cv2.getTrackbarPos("Threshold", "Thresholded Image")

    # Call the threshold callback function
    threshold_callback(threshold_value)

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the window and exit
cv2.destroyAllWindows()
