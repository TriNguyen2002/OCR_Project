import cv2

def capture_frames():
    cap = cv2.VideoCapture(1)  # Use the appropriate camera index (0 for the first camera)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit
            break


capture_frames()
