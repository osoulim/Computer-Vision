import cv2
import numpy as np

cv2.namedWindow("myImage")

cam = cv2.VideoCapture("files/ball.mp4")
lower_bound = np.array([26, 62, 83])
upper_bound = np.array([35, 255, 255])
kernel = np.ones((3, 3), np.uint8)


while True:
    ret, img = cam.read()
    if cv2.waitKey(40) == ord('q') or ret == False:
        break

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv_img, lower_bound, upper_bound)
    erosion = cv2.erode(binary, kernel, iterations=1)
    erosion = cv2.dilate(erosion, kernel, iterations=5)
    cnts, _ = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)
    cv2.imshow("myImage", img)

cam.release()
cv2.destroyAllWindows()
