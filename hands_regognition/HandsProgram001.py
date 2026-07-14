import cv2
import mediapipe as mp
import time

# Инициализация модулей MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mpHands = mp.solutions.hands

# Захват видео с веб-камеры
cap = cv2.VideoCapture(0)

# Даем камере 2 секунды на инициализацию (автофокус, баланс белого)
time.sleep(2)

# Создаем объект детектора рук один раз за пределами цикла
with mpHands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Не удалось получить кадр с камеры")
            break

        # Зеркально отражаем изображение для удобства пользователя
        img = cv2.flip(img, 1)

        # Конвертируем BGR (OpenCV) -> RGB (MediaPipe)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Для повышения производительности помечаем изображение как "только для чтения"
        img_rgb.flags.writeable = False
        results = hands.process(img_rgb)

        # Снимаем флаг только для чтения перед отрисовкой
        img_rgb.flags.writeable = True

        # Если руки найдены
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                # Исправлено имя переменной с hand_landmarks на handLms
                mp_drawing.draw_landmarks(
                    img,
                    handLms,
                    mpHands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2)
                )

        # Отображаем итоговый кадр (в формате BGR)
        cv2.imshow("Picture", img)

        # Выход из программы по нажатию клавиши 'Q' или 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()




