import cv2
import numpy as np

cap = cv2.VideoCapture("eye.mp4")

while cv2.waitKey(30) != ord('q'):
    ret, frame = cap.read()
    if ret is False:
        break
    rows, cols, c = frame.shape
    frame = frame[rows // 4: rows * 3 // 4, cols * 1 // 3: cols * 7 // 10]
    rows, cols, c = frame.shape

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    T, threshold = cv2.threshold(gray_frame, 3, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(cnt)

        if x + w//2 > cols * 6 // 10:
            text = "Right"
        elif x + w//2 < cols * 5 // 10:
            text = "Left"
        else:
            text = "Center"

        cv2.putText(frame, text, (10, 10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(frame, (x + w//2, 0), (x + w//2, rows), (0, 255, 0), 2)
        cv2.line(frame, (0, y + h//2), (cols, y + h//2), (0, 255, 0), 2)

    cv2.imshow("Threshold", frame)


cv2.destroyAllWindows()
