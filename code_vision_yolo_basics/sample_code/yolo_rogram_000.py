import torch
from ultralytics.nn.tasks import DetectionModel

# Для PyTorch 2.6+ обязательно регистрируем класс безопасности
torch.serialization.add_safe_globals([DetectionModel])

from ultralytics import YOLO

# Используем старый формат .pt вместо .safetensors
model = YOLO('../yolov8n.pt')
results = model("images/cars001.jpg", show=True)