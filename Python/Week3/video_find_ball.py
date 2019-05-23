import cv2
import numpy as np

cv2.namedWindow("myImage")

cam = cv2.VideoCapture("ball.mp4")
lower_bound = np.array([26, 62, 83])
upper_bound = np.array([35, 255, 255])
kernel = np.ones((3, 3), np.uint8)

shape = "circle"

while True:
    ret, img = cam.read()
    if cv2.waitKey(40) == ord('q') or ret == False:
        break

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv_img, lower_bound, upper_bound)
    erosion = cv2.erode(binary, kernel, iterations=1)
    erosion = cv2.dilate(erosion, kernel, iterations=5)
    cnts, _ = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        epsilon = cv2.arcLength(c, closed=True) * 0.01
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4:
            shape = "square"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        cv2.putText(img, shape, (20, 20),
                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
        (x, y), radius = cv2.minEnclosingCircle(c)
        cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 3)
        # cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
        # print(cv2.contourArea(c), cv2.arcLength(c, closed=True))
    cv2.imshow("myImage", img)

cam.release()
cv2.destroyAllWindows()
