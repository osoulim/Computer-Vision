import cv2
import numpy as np

cv2.namedWindow("myImage")

cam = cv2.VideoCapture("files/ball.mp4")
lower_bound = np.array([26, 62, 83])
upper_bound = np.array([35, 255, 255])

while True:
    ret, img = cam.read()
    if cv2.waitKey(40) == ord('q') or ret == False:
        break

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv_img, lower_bound, upper_bound)
    binary_3c = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    find_ball = cv2.bitwise_and(img, binary_3c)

    cv2.imshow("myImage", find_ball)

cam.release()
cv2.destroyAllWindows()
