import torch
from ultralytics.nn.tasks import DetectionModel

# Для PyTorch 2.6+ обязательно регистрируем класс безопасности
torch.serialization.add_safe_globals([DetectionModel])

from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()

    results = model(img, show=False)
    annotated_frame = results[0].plot()

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)


    cv2.imshow("Picture", annotated_frame)
    cv2.waitKey(1)

