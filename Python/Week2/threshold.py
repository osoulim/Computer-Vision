import cv2
import numpy as np

cv2.namedWindow("myImage")
img = cv2.imread("files/ball.PNG")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
T, thresh = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)

cv2.imshow("myImage", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
