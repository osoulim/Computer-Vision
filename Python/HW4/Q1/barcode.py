import cv2
import numpy as np
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "Files/barcode_01.jpg"


img = cv2.imread(file)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(grey, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobelY = cv2.Sobel(grey, cv2.CV_64F, dx=0, dy=1, ksize=3)

edges = cv2.subtract(sobelX, sobelY)
edges = cv2.convertScaleAbs(edges)

edges = cv2.blur(edges, (9, 9))
_, thresh = cv2.threshold(edges, 200, 255, cv2.THRESH_BINARY)

morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((10, 30)))
morph = cv2.erode(morph, np.ones((3, 3)))
# morph = cv2.dilate(morph, np.ones((3, 3)))


_, cnt, _ = cv2.findContours(
    morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
maxCountor = max(cnt, key=cv2.contourArea)

maxRect = cv2.minAreaRect(maxCountor)
box = cv2.boxPoints(maxRect).astype(int)
cv2.drawContours(img, [box], -1, (0, 255, 255), 3)
# x, y, w, h = cv2.boundingRect(maxCountor)

# cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

cv2.imshow("barcode", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
