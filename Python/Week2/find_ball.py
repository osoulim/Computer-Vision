import cv2
import numpy as np

cv2.namedWindow("morph")

lower_bound = np.array([26, 62, 83])
upper_bound = np.array([35, 255, 255])

img = cv2.imread("files/ball.PNG")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
binary = cv2.inRange(hsv_img, lower_bound, upper_bound)

kernel = np.ones((3, 3), np.uint8)

# cv2.createTrackbar("erode", "morph", 1, 10, lambda x: x)
# while cv2.waitKey(30) != ord('q'):
#     iterations = cv2.getTrackbarPos("erode", "morph")

erosion = cv2.erode(binary, kernel, iterations=1)
erosion = cv2.dilate(erosion, kernel, iterations=5)

cnts, _ = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

cv2.imshow("morph", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
