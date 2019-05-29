import cv2
import numpy as np
import imutils

segW, segH = 40, 10
seven_segment = [
    ((0, 0), "h"),
    ((0, 0), "v"),
    ((segW - segH, 0), "v"),
    ((0, segW - segH), "h"),
    ((0, segW - segH), "v"),
    ((segW - segH, segW - segH), "v"),
    ((0, 2 * segW - segH), "h")
]

numbers = [
    (0, 1, 2, 4, 5, 6),
    (2, 5),
    (0, 2, 3, 4, 6),
    (0, 2, 3, 5, 6),
    (1, 2, 3, 5),
    (0, 1, 3, 5, 6),
    (0, 1, 3, 4, 5, 6),
    (0, 2, 5),
    (0, 1, 2, 3, 4, 5, 6),
    (0, 1, 2, 3, 5, 6)
]

color_image = cv2.imread("cooler.PNG")
img = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, 200, 255)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

for contour in cnts:
    arc = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * arc, True)
    if len(approx) == 4:
        p1, p2, p3, p4 = approx
        x1 = min(p1[0][0], p2[0][0])
        y1 = min(p1[0][1], p2[0][1])
        x2 = max(p3[0][0], p4[0][0])
        y2 = max(p3[0][1], p4[0][1])
        display = img[y1: y2, x1: x2]
        color_display = color_image[y1: y2, x1: x2]
        break

_, thresh = cv2.threshold(display, 60, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((3, 3)))

contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
boxes = sorted(map(cv2.boundingRect, contours))
for box in boxes:
    x, y, w, h = box
    if w > 10 and 20 < h < 30:
        digit = cv2.resize(thresh[y: y + h, x: x + w], (segW, 2 * segW))
        segments = []
        for i in range(7):
            (x1, y1), align = seven_segment[i]
            w1 = segW if align == "h" else segH
            h1 = segW if align == "v" else segH
            thresh_part = digit[y1: y1 + h1, x1: x1 + w1]
            if np.count_nonzero(thresh_part) / (segW * segH) > 0.5:
                segments.append(i)
        segments = tuple(segments)
        if segments in numbers:
            num = numbers.index(segments)
            cv2.rectangle(color_display, (x, y),
                          (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(color_display, str(num), (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("cropped", imutils.resize(color_display, width=300))
cv2.waitKey(0)
cv2.destroyAllWindows()
