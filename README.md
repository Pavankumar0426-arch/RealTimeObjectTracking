# 🚀 Real-Time Object Detection & Multi-Object Tracking with People Counting

## Overview
This project demonstrates a **real-time object detection and multi-object tracking system** using **YOLOv8** and **DeepSORT**.  
It also implements **bidirectional people counting**, which counts people crossing a virtual line in **both directions**.

---

## ✨ Features
- ✅ Real-time object detection using YOLOv8 (pretrained COCO model).  
- ✅ Multi-object tracking with **unique IDs** using DeepSORT.  
- ✅ **Bidirectional people counting** (upward and downward crossings).  
- ✅ Live video display with bounding boxes, IDs, and counts.  
- ✅ Annotated video saved to `outputs/` for later review.  

---

## 📁 Folder Structure

RealTimeObjectTracking/
├── src/
│ └── multi_track_count_bidirectional.py # Main script
├── models/
│ └── yolov8n.pt # YOLO model (auto-download works)
├── outputs/
│ └── people_count_bidirectional.mp4 # Annotated output video
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml

---

## ⚙️ Installation

1. **Create and activate a virtual environment**:
```
python -m venv objtrack_env
objtrack_env\Scripts\activate       # Windows
# source objtrack_env/bin/activate  # Linux/macOS
```
2. **Install dependencies**:
```
pip install -r requirements.txt
```

4. **▶️ Usage**
```
Navigate to the src/ folder:
cd src

Run the main script:
python multi_track_count_bidirectional.py

The webcam will open:
People will be tracked with bounding boxes and unique IDs.
The counting line will detect upward and downward crossings.
Counts will display live on the video.

Press q to stop the webcam.

The annotated video will be saved in:

outputs/people_count_bidirectional.mp4
🔧 Optional Customizations
Change the counting line position in the script (line_position).
Filter other object classes by COCO class ID (0 = person, 1 = bicycle, 2 = car, etc.).
Adjust YOLOv8 model (yolov8n.pt, yolov8s.pt, etc.) for speed vs accuracy.
Add trajectory lines for each tracked person.
```
## **🛠 Requirements:**
1. Python 3.8+
2. Webcam
3. GPU recommended for faster YOLOv8 inference

## **Dependencies**

1. lua
2. Copy code
3. ultralytics
4. opencv-python
5. opencv-python-headless
6. numpy
7.torch
8. torchvision
9. deep-sort-realtime

## **🔗 References**
1. YOLOv8 Documentation
2. DeepSORT Realtime Tracker
3. COCO Dataset Class IDs

## 👤 Author

### M. PAVAN KUMAR
Python & Computer Vision Enthusiast
