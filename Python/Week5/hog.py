import cv2
from skimage import feature
import imutils
import numpy as np

img = cv2.imread("files/rasht.jpg")
img = imutils.resize(img, width=900)

H, hogImage = feature.hog(img, orientations=8, pixels_per_cell=(10, 10),
                          cells_per_block=(3, 3), block_norm="L1", transform_sqrt=True, visualize=True)

cv2.imshow("test", hogImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
