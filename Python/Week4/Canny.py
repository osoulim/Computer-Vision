import cv2
import numpy as np
import imutils

cv2.namedWindow("edge")
img = cv2.imread("files/lena.bmp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.createTrackbar("low", "edge", 100, 300, lambda x: x)
cv2.createTrackbar("high", "edge", 200, 300, lambda x: x)

while cv2.waitKey(30) != ord('q'):
    low = cv2.getTrackbarPos("low", "edge")
    high = cv2.getTrackbarPos("high", "edge")
    canny = cv2.Canny(gray_img, low, high)
    cv2.imshow("edge", canny)

cv2.destroyAllWindows()
