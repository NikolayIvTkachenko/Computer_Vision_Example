#import torch

import cv2
import numpy as np
import os

#torch.serialization.add_safe_globals([YOLO])

import os
os.environ['PYTORCH_WEIGHTS_ONLY'] = '0'

from ultralytics import YOLO

#model = YOLO('yolov8n.pt')
model = YOLO('../yolov8n.safetensors')
results = model("images/cars001.jpg", show=True)

#checkpoint = torch.load('yolov8n.pt', map_location='cpu',  weights_only=False)
#raw_model = checkpoint['model']
#yolo_wrapper = YOLO(raw_model)
#results = yolo_wrapper("images/cars001.jpg", show=True)
