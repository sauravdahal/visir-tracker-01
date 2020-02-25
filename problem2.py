# Problem 2

import cv2
import sys
import time

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

frame_counter = 0
a = time.time()
while True:

    ret, frame = capture.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    frame_counter += 1

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    
    cv2.imshow('FaceDetection', frame)

    if k % 256 == 27:
        break

    
    if (time.time() - a >= 2):
        print(frame_counter / (time.time() - a))
        a = time.time()
        frame_counter = 0
    

capture.release()
cv2.destroyAllWindows()
