import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    #print(results.multi_hand_landmarks)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )


    cv2.imshow("Picture", img)
    cv2.waitKey(1)