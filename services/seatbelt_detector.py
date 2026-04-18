from ultralytics import YOLO

model = YOLO("models/seatbelt.pt")

def detect_seatbelt(image):
    return model(image, conf=0.25)