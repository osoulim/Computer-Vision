import sys
import cv2
import imutils
import numpy as np


def png2white(image):
    alpha_channel = image[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 254, 255,
                            cv2.THRESH_BINARY)  # binarize mask
    color = image[:, :, :3]
    image = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
    return image


def image_preproccess(image):
    # Grayscale image and put a treshold on it
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY_INV)

    # cv2.imshow("image", thresh)

    # Find contours and get max area contour as number
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return -1
    number = max(contours, key=cv2.contourArea)

    # Rotate image if contour is rotated with min area rectange
    (x, y), (width, height), degree = cv2.minAreaRect(number)
    if width < height:
        thresh = imutils.rotate(thresh, degree)

    # cv2.imshow("rotated", thresh)

    # Find number again in rotated image and crop it
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    number = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(number)
    thresh = thresh[y: y + h, x: x+w]

    if h < w:
        thresh = imutils.rotate_bound(thresh, 90)

    # cv2.imshow("cropped", thresh)
    return thresh


def sampler():
    result = []
    for i in range(10):
        image = cv2.imread("good/%d.PNG" % i)
        image = png2white(image)
        number = image_preproccess(image)
        h, w = number.shape
        print(h, w)
        sampled = []
        for y in range(12, h, 25):
            tmp = []
            for x in range(12, w, 25):
                print(x, y)
                tmp.append(1 if number[y][x] > 100 else 0)
            sampled.append(tmp)
        print(sampled)
        result.append(sampled)
    return result


def digit_recognize(image):
    number = imutils.resize(image_preproccess(image), width=120)
    number_reverse = imutils.rotate_bound(number, 180)
    cv2.imshow("number", number)
    cv2.imshow("reverse", number_reverse)


def main():
    if len(sys.argv) < 2:
        print("Please pass an image path")
        return

    imagePath = sys.argv[1]
    image = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
    h, w, c = image.shape
    if h == 0 or w == 0:
        print("Invalid image path or file")
        return
    image = png2white(image)
    print(digit_recognize(image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
