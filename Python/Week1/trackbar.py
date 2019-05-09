# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:59:17 2019

@author: Mamzi
"""

import cv2


def callback(value): 
    if value == 1:
        cv2.namedWindow("greyFrame")
        gray = cv2.imread("images/pic.jpg", 0)
        cv2.imshow("greyFrame", gray)
        cv2.waitKey(3000)
        cv2.destroyWindow("greyFrame")


img = cv2.imread("images/pic.jpg")


cv2.imshow("frame", img)
cv2.createTrackbar("color/grey", "frame", 0, 1, callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
