import cv2
import numpy as np
import imutils

book = cv2.imread("files/ielts.jpg")
sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(book, None)

cap = cv2.VideoCapture("files/conv.mp4")

videoSift = cv2.xfeatures2d.SIFT_create()

while cv2.waitKey(30) != ord('q'):
    ret, frame = cap.read()
    if not ret:
        break
    h, w, c = frame.shape
    minX, minY = int(0.2 * w), int(0.2 * h)
    maxX, maxY = int(0.8 * w), int(0.8 * h)
    roi = frame[minY: maxY, minX: maxX]
    vidKp, vidDes = videoSift.detectAndCompute(roi, None)
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
    knn = bf.knnMatch(des, vidDes, k=2)
    match, points = [], []
    for m, n in knn:
        if m.distance < 0.6 * n.distance:
            match.append(m)

    frame = cv2.flip(frame, 1)
    cv2.putText(frame, str(len(match)), (minX, minY - 10),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

    color = (0, 255, 0) if len(match) > 20 else (0, 255, 255)
    cv2.rectangle(frame, (minX, minY), (maxX, maxY), color, 3)
    cv2.imshow("Sift", frame)

cv2.destroyAllWindows()
