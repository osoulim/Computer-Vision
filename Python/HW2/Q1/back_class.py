import cv2
import numpy as np
import imutils

cv2.namedWindow("Move detector")
cam = cv2.VideoCapture("back.mp4")

ret, main_frame = cam.read()
main_frame = imutils.resize(main_frame, width=600)

while cv2.waitKey(30) != ord('q'):
    ret, frame = cam.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=600)
    dif = cv2.absdiff(frame, main_frame)
    gray_dif = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_dif, 60, 255, cv2.THRESH_BINARY)

    cnts, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts):
        bozorgVar = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(bozorgVar)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)

    cv2.imshow("Move detector", frame)

cv2.destroyAllWindows()
