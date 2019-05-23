import cv2
import numpy as np

lower = np.array([0, 48, 50], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")


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

    cv2.circle(bin_frame, (x_bar, y_bar), int(distance * 0.7), 0, -1)

    cv2.imshow("Bin", bin_frame)

    fingers, _ = cv2.findContours(
        bin_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    finger_count = len(fingers) - 1

    return finger_count


cv2.namedWindow("Hand")

# cam = cv2.VideoCapture("hand_pic/hand_vid.mp4")
cam = cv2.VideoCapture("hand.mp4")

_, main_frame = cam.read()
h, w, c = main_frame.shape
main_frame = main_frame[0: w, 0: h//2]


while cv2.waitKey(30) != ord('q'):
    ret, frame = cam.read()
    if ret == False:
        break
    frame = frame[0: w, 0: h//2]
    diff = cv2.absdiff(frame, main_frame)
    finger_count = hand_recognition(diff)
    cv2.putText(frame, str("%d fingers" % finger_count), (10, 20),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Hand", diff)

cv2.destroyAllWindows()
