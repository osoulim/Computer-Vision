import cv2
import numpy as np

cv2.namedWindow("Move detector")
cam = cv2.VideoCapture("back.mp4")


while cv2.waitKey(40) != ord('q'):
    ret, main_frame = cam.read()
    main_frame = cv2.cvtColor(main_frame, cv2.COLOR_BGR2GRAY).astype(np.int16)
    if ret == False:
        break

    ret, frame = cam.read()
    if ret == False:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.int16)

    dif = main_frame - gray_frame
    # dif = np.maximum(np.zeros(dif.shape), dif)
    dif = np.abs(dif)

    res, thresh = cv2.threshold(dif, 25, 255, cv2.THRESH_BINARY)
    thresh = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=5)
    points = np.nonzero(thresh)
    if len(points[0]) > 0 and len(points[1]) > 0:
        x_min, x_max = min(points[1]), max(points[1])
        y_min, y_max = min(points[0]), max(points[0])
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)
    cv2.imshow("Move detector", frame)

cv2.destroyAllWindows()
