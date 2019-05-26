import sys
import cv2
import imutils
import numpy as np


def main():
    if len(sys.argv) < 2:
        print("Please pass an image path")
        return

    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
    h, w, c = image.shape
    if h == 0 or w == 0:
        print("Invalid image path or file")
        return

    cv2.namedWindow("digit")
    cv2.imshow("digit", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
