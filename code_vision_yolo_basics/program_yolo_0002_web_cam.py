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
    cv2.imshow("Picture", annotated_frame)
    cv2.waitKey(1)






#-------------------------------------------------------------------------
#results = model(img, stream=True)