import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow("Colors")
cv2.createTrackbar("H", "Colors", 0, 179, nothing)
cv2.createTrackbar("S", "Colors", 255, 255, nothing)
cv2.createTrackbar("V", "Colors", 255, 255, nothing)

height, width = 256, 360
img_hsv = np.zeros((height, width, 3), dtype=np.uint8)

while True:

    h = cv2.getTrackbarPos("H", "Colors")
    s = cv2.getTrackbarPos("S", "Colors")
    v = cv2.getTrackbarPos("V", "Colors")

    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("Colors", img_bgr)
    key = cv2.waitKey(1)
    if key == 27:
        break