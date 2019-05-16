import cv2
import numpy as np

cv2.namedWindow("myImage")
img1 = cv2.imread("files/circle.png")
img2 = cv2.imread("files/rectangle.png")

and_img = cv2.bitwise_and(img1, img2)
or_img = cv2.bitwise_or(img1, img2)
xor_img = cv2.bitwise_xor(img1, img2)
not_img = cv2.bitwise_not(img1)


cv2.imshow("myImage", not_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
