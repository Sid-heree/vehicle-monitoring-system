from services.vehicle_detector import detect_vehicle
from services.plate_detector import detect_plate
from services.ocr_reader import read_text
from services.seatbelt_detector import detect_seatbelt

import cv2

def process_image(image, use_ocr=True):

    results = detect_vehicle(image)
    annotated_image = image.copy()

    final_results = []

    boxes = results[0].boxes
    allowed_classes = ["car", "truck", "bus", "motorcycle"]

    if boxes is None:
        return {"image": annotated_image, "data": []}

    for i, v in enumerate(boxes.xyxy):

        cls_id = int(boxes.cls[i])
        vehicle_type = results[0].names[cls_id]

        if vehicle_type not in allowed_classes:
            continue

        x1, y1, x2, y2 = map(int, v)
        crop = image[y1:y2, x1:x2]

        # 🔤 Plate
        plate_text = "Not detected"
        plate_result = detect_plate(crop)

        if plate_result and len(plate_result) > 0:
            if plate_result[0].boxes is not None and len(plate_result[0].boxes) > 0:

                if use_ocr:
                    px1, py1, px2, py2 = map(int, plate_result[0].boxes.xyxy[0])
                    plate_crop = crop[py1:py2, px1:px2]

                    text = read_text(plate_crop)
                    if text:
                        plate_text = text[0][1]
                else:
                    plate_text = "Plate Detected"

        # 🪑 Seatbelt
        seatbelt_status = "Not detected"
        seatbelt_result = detect_seatbelt(crop)

        if seatbelt_result and len(seatbelt_result) > 0:
            if seatbelt_result[0].boxes is not None and len(seatbelt_result[0].boxes) > 0:
                classes = seatbelt_result[0].boxes.cls.tolist()

                if 1 in classes:
                    seatbelt_status = "Seatbelt ON"
                else:
                    seatbelt_status = "Seatbelt OFF"

        final_results.append({
            "vehicle_type": vehicle_type,
            "plate": plate_text,
            "seatbelt": seatbelt_status
        })

        # 🔥 Draw box
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

        label = f"{vehicle_type} | {plate_text} | {seatbelt_status}"

        # 🔥 Better label visibility
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

        cv2.rectangle(
            annotated_image,
            (x1, y1 - h - 10),
            (x1 + w, y1),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated_image,
            label,
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

    return {"image": annotated_image, "data": final_results}