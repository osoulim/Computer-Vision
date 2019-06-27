import cv2
import dlib
import numpy as np
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("files/shape_predictor_68_face_landmarks.dat")

img = cv2.imread("files/face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = imutils.resize(gray, width=300) 

rects = detector(gray, 0)

for face in rects:
    x1, y1 = face.left(), face.top()
    x2, y2 = face.right(), face.bottom()

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3 )

    shape = predictor(gray, face)
    shape = face_utils.shape_to_np(shape)
    cX, cY = shape.mean(axis=0, dtype="int")
    last = (cX, cY)
    for x,y in shape:
        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        cv2.line(img, (cX, cY), (x, y), (0, 255, 255), 1)
        # cv2.line(img, last, (x, y), (255, 0, 0), 1)
        # last = (x, y)
    cv2.circle(img, (cX, cY), 3, (255, 0, 0), -1)

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
