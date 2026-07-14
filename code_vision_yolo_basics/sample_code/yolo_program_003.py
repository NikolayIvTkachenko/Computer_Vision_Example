import os
from ultralytics import YOLO

weights_path = '../yolov8n.safetensors'

if not os.path.exists(weights_path):
    print(f"Файл {weights_path} не найден в текущей директории.")
    # Здесь можно вызвать автоматическое скачивание через YOLO('yolov8n')
else:
    print("Файл найден, загружаем модель...")
    model = YOLO(weights_path)
    results = model("images/cars001.jpg", show=True)