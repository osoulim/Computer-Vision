import cv2
import numpy as np

img = cv2.imread("pic1.jpg")
h, w, c = img.shape
b, g, r = cv2.split(img)

gray = np.asarray([[(b[x][y] * 0.114 + g[x][y] * 0.587 + r[x][y] * 0.299)
                    for y in range(h)] for x in range(w)])

cv2.imwrite("gray.jpg", gray)
