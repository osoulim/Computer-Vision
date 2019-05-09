# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:01:58 2019

@author: Mamzi
"""

import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("webcam")

while True:
    ret, frame = cap.read()
    if ret == False or cv2.waitKey(5) == ord('q'):
        break
    cv2.imshow("webcam", frame)

cap.release();
cv2.destroyAllWindows()
