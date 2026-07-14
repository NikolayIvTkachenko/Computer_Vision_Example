import torch
from ultralytics.nn.tasks import DetectionModel

# Для PyTorch 2.6+ обязательно регистрируем класс безопасности
torch.serialization.add_safe_globals([DetectionModel])

from ultralytics import YOLO

import cv2

# Используем старый формат .pt вместо .safetensors
model = YOLO('yolov8n.pt')
#model = YOLO('yolov8n.pt', device='cpu') # или '0' для первого GPU
results = model("images/cars001.jpg", show=False)

annotated_frame = results[0].plot()

# Выводим через OpenCV
cv2.imshow('YOLO Result', annotated_frame)
cv2.waitKey(0) # Теперь эта строка работает корректно
cv2.destroyAllWindows()