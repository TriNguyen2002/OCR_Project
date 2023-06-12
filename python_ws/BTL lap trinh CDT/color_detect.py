import cv2
import numpy as np
import mask
count = 0

# open camera
cap = cv2.VideoCapture(0)
while True:
    a, frame = cap.read()
    # hsv color transform
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#   create a mask of the red color

    result = cv2.bitwise_and(frame,frame, mask=mask.rmask(hsv))
    cv2.imshow("img",result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #   screenshots
    # if cv2.waitKey(1) & 0xFF== ord('s'):
    #         img_name = "Resources/test_pic_{}.jpg".format(count)
    #         count +=1
    #         cv2.imwrite(img_name,frame)

cap.release()
cv2.destroyAllWindows()