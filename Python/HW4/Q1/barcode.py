import cv2
import numpy as np

img = cv2.imread("Files/barcode_04.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(grey, cv2.CV_64F, dx=1, dy=0, ksize=-3)
sobelY = cv2.Sobel(grey, cv2.CV_64F, dx=0, dy=1, ksize=-3)

edges = cv2.subtract(sobelX, sobelY)
edges = cv2.convertScaleAbs(edges)

edges = cv2.blur(edges, (9, 9))
_, thresh = cv2.threshold(edges, 220, 255, cv2.THRESH_BINARY)

closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((7, 21)))


_, cnt, _ = cv2.findContours(
    closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

maxCountor = max(cnt, key=cv2.contourArea)


x, y, w, h = cv2.boundingRect(maxCountor)

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

cv2.imshow("barcode", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
