from ultralytics import YOLO
import cv2

# Load YOLOv8n model (pretrained on COCO)
model = YOLO("yolov8n.pt")  # You can also use yolov8s.pt if you want better accuracy

def detect_ships(image_path, conf_threshold=0.25):
    # Read image
    img = cv2.imread(image_path)

    # Run inference
    results = model(image_path)[0]

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        if conf >= conf_threshold:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = model.names[cls_id]
            detections.append({
                'label': label,
                'confidence': conf,
                'box': [x1, y1, x2, y2]
            })

    return img, detections
