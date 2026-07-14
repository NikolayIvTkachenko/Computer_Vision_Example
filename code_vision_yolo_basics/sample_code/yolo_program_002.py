from ultralytics import YOLO



# Используем файл .safetensors вместо .pt
model = YOLO('../yolov8n.safetensors')

results = model("images/cars001.jpg", show=True)


