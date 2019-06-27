from scipy.spatial import distance as dist 
import cv2
import dlib
from imutils import face_utils, resize, rotate
import numpy as np

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

COUNTER = 0
TOTAL = 0

def eye_aspect_ratio(eye):
    return (dist.euclidean(eye[1], eye[5]) + dist.euclidean(eye[2], eye[4])) / (2.0 * dist.euclidean(eye[0], eye[3]))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("files/shape_predictor_68_face_landmarks.dat")

cam = cv2.VideoCapture(0)

while cv2.waitKey(30) != ord('q'):
    ret, frame = cam.read()
    if not ret: 
        break

    # frame = rotate(frame, angle=-90)
    frame = resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)
    
    for face in rects:
        p1 = (face.left(), face.top())
        p2 = (face.right(), face.bottom())
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
        
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[36:42]
        rightEye = shape[42:48]

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull, rightEyeHull], -1, (0, 255, 255), 2)

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        meanEAR = (rightEAR + leftEAR) / 2.0

        if meanEAR < EYE_AR_THRESH:
            COUNTER += 1
        elif COUNTER > EYE_AR_CONSEC_FRAMES:
            TOTAL += 1
            COUNTER = 0
        
        cv2.putText(frame, str(meanEAR), (0, 20),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, str(TOTAL), (0, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)



    cv2.imshow("video", frame)


cam.release()
cv2.destroyAllWindows()
