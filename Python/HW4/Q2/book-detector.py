# import cv2.cv2 as cv2
import cv2
import numpy as np
import imutils

img = cv2.imread("files/book3.jpg")
img = cv2.resize(img, (300, 480))
# cv2.imshow("book", img)
sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(img, None)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('files/output.mp4', fourcc,
                      20.0, (940, 480))


while cv2.waitKey(20) != ord('q'):
    ret, frame = cap.read()
    if not ret:
        break
    frame = imutils.resize(frame, height=480)
    videoSift = cv2.xfeatures2d.SIFT_create()
    videoKp, videoDes = videoSift.detectAndCompute(frame, None)
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
    knn = bf.knnMatch(des, videoDes, k=2)
    match, points = [], []
    for m, n in knn:
        if m.distance < 0.6 * n.distance:
            match.append(m)
            points.append(tuple(map(int, videoKp[m.trainIdx].pt)))
    if len(match) > 10:
        # result = cv2.drawMatches(img, kp, frame, videoKp, match,
        #                          None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

        xMin, yMin, xMax, yMax = min((p[0] for p in points)), min(
            (p[1] for p in points)), max((p[0] for p in points)), max((p[1] for p in points))
        cv2.rectangle(frame, (xMin, yMin), (xMax, yMax), (0, 255, 255), 3)
    res = np.concatenate((img, frame), 1)
    cv2.imshow("video", res)
    out.write(res)
