from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # fast model

def detect_vehicle(image):
    return model(image, conf=0.25)