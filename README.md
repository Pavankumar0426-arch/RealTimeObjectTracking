# 🚀 Real-Time Object Detection & Multi-Object Tracking with People Counting

## 📄 Abstract
This project implements a Real-Time Object Detection and Multi-Object Tracking system with Bidirectional People Counting using YOLOv8 and DeepSORT. The system is designed to accurately detect people in live video streams, assign unique IDs to track multiple objects simultaneously, and count the number of people crossing a virtual line in both directions.

The main objectives of this project are:
1. Accurate Detection: Utilize YOLOv8’s fast and precise detection capability to identify people in real time.
2. Robust Tracking: Track multiple people simultaneously with DeepSORT, maintaining unique IDs even in cases of occlusion or crossing paths.
3. Bidirectional Counting: Count people moving both upward and downward across a virtual line, providing insights into traffic flow.
4. Visualization: Display bounding boxes, track IDs, and real-time counts on live video. Additionally, store annotated videos for offline analysis.
5. Analytics: Generate people count graphs over time to analyze patterns and trends.

This project can be applied in smart surveillance, crowd management, retail analytics, and public space monitoring, providing both real-time alerts and historical insights into human movement patterns.

---
## ✨ Features
- ✅ Real-time object detection with **YOLOv8**  
- ✅ Multi-object tracking with **DeepSORT** and unique IDs  
- ✅ Bidirectional people counting (up/down crossings)  
- ✅ Live annotated video display with bounding boxes, IDs, and counts  
- ✅ Save annotated video for analysis in `outputs/`  


## 📁 Folder Structure
```
RealTimeObjectTracking/
├── src/
│ └── multi_track_count_bidirectional.py # Main script
├── models/
│ └── yolov8n.pt # YOLO model (auto-download works)
├── outputs/
<<<<<<< HEAD
│ └── people_count_bidirectional.mp4
├── requirements.txt
└── README.md
```

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

3. **▶️ Usage**
```


Install dependencies:
pip install -r requirements.txt

▶️ Usage

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
