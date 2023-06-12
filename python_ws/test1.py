import cv2 as cv

def rescale(frame, scale = 0.2):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)
    dim = (w,h)
    return cv.resize(img, dim, interpolation=cv.INTER_AREA)

img = cv.imread('Resources\murakami_book.jpg')
count = 0

# Reading Videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF==ord('d'):
            break            
        if cv.waitKey(1) & 0xFF== ord('s'):
            img_name = "Resources/test_pic_{}.jpg".format(count)
            count +=1
            cv.imwrite(img_name,frame)


capture.release()
cv.destroyAllWindows()
