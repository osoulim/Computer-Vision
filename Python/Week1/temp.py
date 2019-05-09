# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

cv2.namedWindow("opencv test")

img = cv2.imread("images/pic.jpg")

#cv2.line(img, (30, 30), (200, 150), (0, 255, 0), 5)

cv2.rectangle(img, (400, 410), (600, 600), (0, 255, 0), 3)
#cv2.circle(img,(200, 150), 100, (255, 0, 0), 5)
cv2.rectangle(img, (400, 375), (600, 410), (0, 255, 0), -1)
cv2.putText(img, "detected", (400, 400), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)


cv2.imshow("opencv test", img)

cv2.waitKey(0)

#cv2.destroyWindow("opencv test")

cv2.destroyAllWindows()

