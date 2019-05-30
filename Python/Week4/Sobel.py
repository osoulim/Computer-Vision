import cv2
import numpy as np
import imutils

cv2.namedWindow("edge")

img = cv2.imread("files/simple_square.png")
resized_img = imutils.resize(img, width=500)

gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(gray_img, cv2.CV_64F, dx=0, dy=1, ksize=3)
sobelX = cv2.convertScaleAbs(sobelX)
sobelY = cv2.Sobel(gray_img, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobelY = cv2.convertScaleAbs(sobelY)


cv2.imshow("edge", sobelX)
cv2.waitKey(0)
cv2.destroyAllWindows()
