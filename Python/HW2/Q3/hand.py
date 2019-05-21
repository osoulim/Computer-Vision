import cv2
import numpy as np

kernel = np.ones((3, 3))


def hand_recognition(frame):
    B, G, R = cv2.split(frame)
    RG = R / G
    bin_frame = cv2.inRange(RG, 1.55, 4)
    bin_frame = cv2.morphologyEx(bin_frame, cv2.MORPH_OPEN, kernel)

    cntrs, _ = cv2.findContours(
        bin_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(cntrs) == 0:
        return 0

    hand = max(cntrs, key=cv2.contourArea)
    x_bar = int(np.average([x[0][0] for x in hand]))
    y_bar = int(np.average([x[0][1] for x in hand]))

    distance = max(
        (np.linalg.norm([x_bar - x[0][0], y_bar - x[0][1]]) for x in hand))

    radius = int(distance * 0.7)

    cv2.circle(bin_frame, (x_bar, y_bar), int(distance * 0.7), 0, -1)

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
cam = cv2.VideoCapture("hand_pic/hand_vid.mp4")
ret, background = cam.read()
background = background.astype(np.int16)

while ret and cv2.waitKey(30) != ord('q'):
    ret, frame = cam.read()
    if ret == False:
        break
    h, w, c = frame.shape
    cropped = frame[0: h // 2, 0: w]

    # sub_image = np.abs(frame.astype(np.int16) - background)

    finger_count = hand_recognition(cropped)
    cv2.putText(cropped, str("%d fingers" % finger_count), (10, 20),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Hand", cropped)

cv2.destroyAllWindows()
