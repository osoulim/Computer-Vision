import cv2
import imutils

cv2.namedWindow("MyImage")

img = cv2.imread("img.jpg")

translated = imutils.translate(img, 25, -75)

cv2.imshow("MyImage", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
