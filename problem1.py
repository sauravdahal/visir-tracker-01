# Problem 1

import cv2
import sys
import time

capture = cv2.VideoCapture(0)

frame_counter = 0
a = time.time()
while True:

    ret, frame = capture.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)

    frame_counter += 1

    cv2.imshow('FaceDetection', frame)

    if k % 256 == 27:
        break

    
    if (time.time() - a >= 2):
        print(frame_counter / (time.time() - a))
        a = time.time()
        frame_counter = 0
    

capture.release()
cv2.destroyAllWindows()
