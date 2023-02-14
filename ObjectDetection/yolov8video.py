from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
#source=0 for webcam but can deal with image files and folders as well
results = model.predict(source="0" ,show=True)
print(results.xyxy[0])