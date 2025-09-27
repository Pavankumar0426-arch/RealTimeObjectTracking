# Real-Time Object Detection & Multi-Object Tracking with People Counting

## Overview
This project demonstrates a **real-time object detection and multi-object tracking system** using **YOLOv8** and **DeepSORT**.  
It also implements **bidirectional people counting**, which counts people crossing a virtual line in both directions.

---

## Features
- Real-time object detection using YOLOv8 (pretrained COCO model).  
- Multi-object tracking with unique IDs using DeepSORT.  
- Bidirectional people counting (upward and downward crossings).  
- Live video display with bounding boxes, IDs, and counts.  
- Annotated video saved to `outputs/` for later review.

---

## Folder Structure
RealTimeObjectTracking/
├── src/
│ └── multi_track_count_bidirectional.py
├── models/
│ └── yolov8n.pt
├── outputs/
│ └── people_count_bidirectional.mp4
├── requirements.txt
└── README.md

yaml
Copy code

---

## Installation

1. **Create and activate a virtual environment**:

python -m venv objtrack_env
objtrack_env\Scripts\activate       # Windows
# source objtrack_env/bin/activate  # Linux/macOS
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Go to the src/ folder:

bash
Copy code
cd src
Run the main script:

bash
Copy code
python multi_track_count_bidirectional.py
The webcam will open:

People will be tracked with bounding boxes and unique IDs.

The counting line will detect upward and downward crossings.

Counts will display live on the video.

Press q to stop the script.

Annotated video will be saved in outputs/people_count_bidirectional.mp4.

Optional Customizations
Change the counting line position in the script (line_position).

Filter other object classes by COCO class ID (0 = person, 1 = bicycle, 2 = car, etc.).

Adjust YOLOv8 model (yolov8n.pt, yolov8s.pt, etc.) for speed vs accuracy.

Add trajectory lines for each tracked person.

Requirements
Python 3.8+

Webcam

GPU recommended for faster YOLOv8 inference

Dependencies:

lua
Copy code
ultralytics
opencv-python
opencv-python-headless
numpy
torch
torchvision
deep-sort-realtime
References
YOLOv8 Documentation

DeepSORT Realtime Tracker

COCO Dataset Class IDs

###Author
M. Pavan Kumar
B.Tech Student | Python & Computer Vision Enthusiast.
