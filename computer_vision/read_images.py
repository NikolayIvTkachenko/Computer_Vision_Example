import cv2

img = cv2.imread("cars001.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", imgGray)

cv2.waitKey(0)