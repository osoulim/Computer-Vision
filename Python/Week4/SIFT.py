import cv2
import numpy as np
import imutils

book1 = cv2.imread("files/book1.jpg")
book2 = cv2.imread("files/book2.JPG")

book1 = imutils.resize(book1, width=500)
book2 = imutils.resize(book2, width=700)
# book2 = cv2.cvtColor(book2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(book1, None)
kp2, desc2 = sift.detectAndCompute(book2, None)

# cv2.drawKeypoints(book1, kp1, book1,
#                   flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
# match = bf.match(desc1, desc2)
# match = sorted(match, key=lambda x: x.distance)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
knn = bf.knnMatch(desc1, desc2, k=2)
match = []
for m, n in knn:
    if m.distance < 0.6 * n.distance:
        match.append(m)

result = cv2.drawMatches(book1, kp1, book2, kp2, match,
                         None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow("book1", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
