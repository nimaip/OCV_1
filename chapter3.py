import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("C:/Users/nimai/Downloads/haar_front.xml")
cap = cv2.VideoCapture(0)
cap.set(4, 600)
cap.set(3, 800)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.putText(img, "Face Detected", (x, y -50), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 3)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


cap.release()