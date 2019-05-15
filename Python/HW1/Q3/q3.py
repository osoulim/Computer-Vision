import cv2
import numpy as np

img = cv2.imread("q2.png")

h, w, c = img.shape
colors = cv2.split(img)

cols = ["Blue", "Green", "Red"]
for index, color in enumerate(colors):
    cells = np.nonzero(color > 100)
    cv2.rectangle(img, (cells[1][0] - 10, cells[0][0] - 10), (cells[1][-1] + 10, cells[0][-1] + 10),
                  (255, 255, 255), 2)
    cv2.putText(img, cols[index], (cells[1][0] - 10, cells[0]
                                   [0] - 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))

cv2.imshow("colors", img)
cv2.imwrite("res.png", img)
cv2.waitKey(0)
