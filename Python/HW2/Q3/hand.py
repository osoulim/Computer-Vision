import cv2
import numpy as np

lower = np.array([0, 48, 50], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def hand_recognition(frame):
    # B, G, R = cv2.split(frame)
    # RG = R / G
    # bin_frame = cv2.inRange(RG, 1.1, 4)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    bin_frame = cv2.inRange(hsv_frame, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    bin_frame = cv2.erode(bin_frame, kernel, iterations=2)
    bin_frame = cv2.dilate(bin_frame, kernel, iterations=2)

    cntrs, _ = cv2.findContours(
        bin_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(cntrs) == 0:
        return 0

    hand = max(cntrs, key=cv2.contourArea)
    x_bar = int(np.average([x[0][0] for x in hand]))
    y_bar = int(np.average([x[0][1] for x in hand]))

    distance = max(
        (np.linalg.norm([x_bar - x[0][0], y_bar - x[0][1]]) for x in hand))

    # cv2.circle(bin_frame, (x_bar, y_bar), int(distance * 0.5), 0, -1)

    cv2.imshow("Bin", bin_frame)

    fingers, _ = cv2.findContours(
        bin_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    finger_count = len(fingers) - 1

    # for x in hand:
    #     cv2.circle(frame, (x[0][0], x[0][1]), 5, (0, 255, 0), 1)

    # cv2.line(frame, (x_bar - 5, y_bar), (x_bar + 5, y_bar), (0, 255, 0), 1)ض
    # cv2.line(frame, (x_bar, y_bar - 5), (x_bar, y_bar + 5), (0, 255, 0), 1)
    return finger_count


cv2.namedWindow("Hand")

# img = cv2.imread("hand_pic/5.jpg")

# cam = cv2.VideoCapture("hand_pic/hand_vid.mp4")
cam = cv2.VideoCapture("hand.mp4")
ret, background = cam.read()
background = background.astype(np.int16)

while ret and cv2.waitKey(30) != ord('q'):
    ret, frame = cam.read()
    if ret == False:
        break
    frame = adjust_gamma(frame, 0.5)
    finger_count = hand_recognition(frame)
    cv2.putText(frame, str("%d fingers" % finger_count), (10, 20),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Hand", frame)

cv2.destroyAllWindows()
