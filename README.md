# 🧠 Real-Time Object Detection using YOLOv8 + Flask + OpenCV

A real-time object detection web application using the YOLOv8n model (`yolov8n.pt`), integrated with Flask and OpenCV. The system captures video from a webcam, processes frames using a lightweight deep learning model, and displays live detection results in a browser.

---

## 🚀 Features

* ⚡ Real-time object detection using [YOLOv8](https://github.com/ultralytics/ultralytics)
* 🖥️ Web interface built with Flask for live video streaming
* 🎯 Lightweight and efficient (`yolov8n.pt`) model for performance on CPUs/GPUs
* 🧠 PyTorch backend for deep learning inference
* 🧪 Customizable to support other YOLO models or trained datasets

---

## 🛠️ Tech Stack

* Python
* Flask
* OpenCV
* PyTorch
* NumPy
* Ultralytics YOLOv8

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/real-time-object-detection.git
cd real-time-object-detection
```
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download YOLOv8n model

The ultralytics package will automatically download yolov8n.pt on the first run.

You can also manually download it from the Ultralytics Model Zoo.

▶️ How to Run
bash
Copy
Edit
python app.py
Then open your browser and go to:

📍 http://localhost:5000/

You’ll see live video with real-time object detection.

📁 Project Structure
php
Copy
Edit
real-time-object-detection/
│
├── app.py                  # Main Flask application
├── yolov8n.pt              # YOLOv8n model (optional if auto-downloaded)
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Optional CSS styling
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
📌 Notes
Model: YOLOv8n (yolov8n.pt) – optimized for speed and resource efficiency

Webcam Required: Ensure your machine has access to a webcam

CUDA Support: For GPU acceleration, install the correct CUDA-enabled PyTorch version

📸 Demo
(Add a GIF or screenshot here if available)

🙌 Acknowledgements
Ultralytics YOLOv8

PyTorch

OpenCV

📃 License
This project is open-source and available under the MIT License.
