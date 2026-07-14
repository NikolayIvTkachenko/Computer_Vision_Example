import cv2

img = cv2.imread("cars001.jpg")

#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(img, (15, 15), 0)

#[y1:y2, x1:x2]
imgCrop = img[100:200, 50:200]

cv2.imshow("Image", img)
cv2.imshow("Image Cro", imgCrop)

cv2.waitKey(0)