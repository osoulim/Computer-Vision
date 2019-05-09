# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:30:10 2019

@author: Mamzi
"""

import cv2

cv2.namedWindow("emoji")


cv2.createTrackbar("paint", "emoji", 0, 3, lambda x: 0)

while True:
    img = cv2.imread("images/emoji.bmp")

    value = cv2.getTrackbarPos("paint", "emoji")
    if value >= 0:
        cv2.circle(img, (250, 250), 200, (0, 0, 0), 1)

    if value >= 1:
        cv2.ellipse(img, (150, 150), (20, 30), 0, 0, 180, (150, 0, 0), -1)
        cv2.ellipse(img, (350, 150), (30, 20), 0, 0, 360, (150, 0, 0), -1)

    if value >= 2:
        cv2.rectangle(img, (230, 210), (270, 290), (0, 150, 0), -1)

    if value >= 3:
        cv2.ellipse(img, (250, 350), (50, 30), 0, 0, 360, (0, 0, 150), -1)

    cv2.imshow("emoji", img)
    if cv2.waitKey(30) == ord('q'):
        break


cv2.destroyWindow("emoji")
