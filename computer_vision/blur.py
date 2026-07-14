import cv2

img = cv2.imread("cars001.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Image", img)
cv2.imshow("Image Blur", imgBlur)

cv2.waitKey(0)