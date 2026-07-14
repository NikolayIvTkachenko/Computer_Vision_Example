import cv2

img = cv2.imread("cars001.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.putText(img, "Test TEXT on Image", (350, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)