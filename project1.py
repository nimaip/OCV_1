import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 130)

myColors = [[5, 107, 0, 19, 255, 255],
            [17, 41, 87, 255, 40, 127],
            [57, 76, 0, 100, 255, 255]]

myPoints = []

def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    lower = np.array(myColors[1][0:3])
    upper = np.array(myColors[1][3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    if x!=0 and y!= 0:
        newPoints.append([x, y])
    cv2.circle(imgResult, (x, y), 20, (255, 0, 0), cv2.FILLED)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = 0, 0, 0, 0
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return (x+w//2), y

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 20, (255, 0, 0), cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints)

    cv2.imshow("Cam", imgResult)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

