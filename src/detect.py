# src/detect.py

import cv2
from ultralytics import YOLO
import os

# Paths
output_dir = "../outputs"
os.makedirs(output_dir, exist_ok=True)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # make sure model is in models/ folder

# Initialize webcam
cap = cv2.VideoCapture(0)

# Video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(os.path.join(output_dir, "video_output.mp4"), fourcc, 20.0, 
                      (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Object detection
    results = model(frame)
    annotated_frame = results[0].plot()  # Draw boxes

    # Show frame
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Save frame to video
    out.write(annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
