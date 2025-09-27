# src/multi_track_count_bidirectional.py

import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize DeepSORT
tracker = DeepSort(max_age=30)

# Initialize webcam
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video writer
out = cv2.VideoWriter("../outputs/people_count_bidirectional.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'), 20.0,
                      (frame_width, frame_height))

# Counting line
line_position = int(frame_height / 2)
cv2_line_color = (0, 0, 255)
line_thickness = 2

# Counters
up_count = 0
down_count = 0

# Store previous center positions of track IDs
track_previous_centers = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    # Filter only people (COCO class 0 = person)
    for box, score, cls in zip(results.boxes.xyxy, results.boxes.conf, results.boxes.cls):
        if int(cls) != 0:
            continue
        x1, y1, x2, y2 = [int(b) for b in box]
        detections.append(([x1, y1, x2 - x1, y2 - y1], float(score), int(cls)))

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw counting line
    cv2.line(frame, (0, line_position), (frame_width, line_position),
             cv2_line_color, line_thickness)

    for track in tracks:
        if not track.is_confirmed():
            continue

        x1, y1, x2, y2 = track.to_ltrb()
        track_id = track.track_id

        # Draw bounding box and ID
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Compute center
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        # Get previous center
        prev_cy = track_previous_centers.get(track_id, None)
        track_previous_centers[track_id] = cy  # Update current center

        if prev_cy is None:
            continue  # Skip first frame for this track

        # Check crossing line
        if prev_cy < line_position <= cy:  # Moving down
            down_count += 1
        elif prev_cy > line_position >= cy:  # Moving up
            up_count += 1

    # Display counts
    cv2.putText(frame, f"Up: {up_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
    cv2.putText(frame, f"Down: {down_count}", (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    # Show frame
    cv2.imshow("People Counting Bidirectional", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
