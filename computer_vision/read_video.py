import cv2

cap = cv2.VideoCapture("auto_fro_camera_short.mp4")

while True:
    success, img = cap. read()

    if not success:
        break

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break