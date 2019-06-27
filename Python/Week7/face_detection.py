import cv2
import dlib
import imutils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("files/shape_predictor_68_face_landmarks.dat")

img = cv2.imread("files/oscar.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = imutils.resize(gray, width=300) 

rects = detector(gray, 0)

for face in rects:
    x1, y1 = face.left(), face.top()
    x2, y2 = face.right(), face.bottom()

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3 )

    shape = predictor(gray, face)

cv2.imshow("face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
