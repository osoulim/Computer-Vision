import cv2
import imutils
import numpy as np

cv2.namedWindow("MyImage")

img = cv2.imread("img.jpg")

# translated = imutils.translate(img, 25, -75)
# rotated = imutils.rotate(img, 45)
img = imutils.resize(img, width=600)
# url_images = imutils.url_to_image(
#     "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png")

kernel = np.ones((4, 4))
# conv = cv2.filter2D(img, cv2.CV_16U, kernel)
blur = cv2.GaussianBlur(img, (5, 5), 1)

cv2.imshow("MyImage", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
