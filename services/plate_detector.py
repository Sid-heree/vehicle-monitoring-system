from ultralytics import YOLO

model = YOLO("models/plate.pt")

def detect_plate(image):
    return model(image, conf=0.25)