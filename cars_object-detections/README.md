# 🚗 Vehicle Counter System - Computer Vision with YOLO

An AI-powered vehicle counting system that detects, tracks, and counts vehicles in videos based on their direction (incoming/outgoing) using YOLOv8.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![YOLO](https://img.shields.io/badge/YOLO-v8-red.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Parameters](#️-parameters)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- 🎯 **Real-time Detection**: Vehicle detection with YOLOv8
- 🔢 **Object Tracking**: Track each vehicle with unique ID
- ↕️ **Direction Detection**: Automatically detect incoming/outgoing directions
- 📊 **Live Statistics**: Real-time counter display on top-right corner
- 🎨 **Visual Output**: Bounding boxes and ID labels
- ⚡ **Fast Processing**: Optimized with GPU support
- 🎬 **Video Export**: Save processed video with annotations

## 🎥 Demo

### Input Video
![Input Video]([https://drive.google.com/file/d/1HE2tud2OjGnd0x_SxK9jlnNtXIx67jna/view?usp=sharing](https://drive.google.com/thumbnail?id=1HE2tud2OjGnd0x_SxK9jlnNtXIx67nja&sz=w600)](https://drive.google.com/file/d/1HE2tud2OjGnd0x_SxK9jlnNtXIx67nja/preview))

### Output Video
![Output Video](https://drive.google.com/file/d/1Amdmjj0pI8fSbzrkqN_NrHKSXZ9a8Iwr/view?usp=sharing)

**Results:**
- 🚗 Outgoing Vehicles: 98
- 🚙 Incoming Vehicles: 108
- 🔢 Total: 206

## 🚀 Installation

### Requirements

```bash
Python 3.8+
CUDA 11.0+ (Optional, for GPU acceleration)
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/username/vehicle-counter.git
cd vehicle-counter
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```txt
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0
torch>=2.0.0
```

### Step 4: Download YOLO Model

The model will be downloaded automatically on first run, or manually:

```bash
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

## 💻 Usage

### Google Colab

1. Open Colab notebook: [Colab Link](#)
2. Run the code
3. Upload your video file
4. Download the processed video

### Local Machine

```bash
python vehicle_counter.py --video path/to/video.mp4
```

### With Parameters

```bash
python vehicle_counter.py \
    --video cars.mp4 \
    --output output_counted.mp4 \
    --line-position 0.5 \
    --model yolov8n.pt \
    --confidence 0.5
```

## 🧠 How It Works

### 1. Video Processing Pipeline

```
Video Input → Frame Extraction → YOLO Detection → Object Tracking → Counting → Video Output
```

### 2. Counting Algorithm

```python
# For each frame:
1. Detect vehicles with YOLO
2. Assign unique ID to each vehicle (tracking)
3. Check bounding box bottom/top edge
4. Did the edge cross the counting line?
   - Top to bottom → OUTGOING +1
   - Bottom to top → INCOMING +1
5. Store counted IDs (prevent double counting)
```

### 3. Visual Algorithm

```
Frame N-1:     Frame N:
  ┌────┐         
  │ 🚗 │       ┌────┐
  └────┘       │ 🚗 │  ← Bottom edge crossed the line
━━━━━━━━━━━━━  └────┘  ✅ COUNTED!
              ━━━━━━━━━━━━━
```

## 📁 Project Structure

```
vehicle-counter/
│
├── vehicle_counter.py      # Main program
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── LICENSE                # License
│
├── models/                # YOLO models
│   └── yolov8n.pt
│
├── input/                 # Input videos
│   └── sample_video.mp4
│
├── output/                # Output videos
│   └── output_counted.mp4
│
└── docs/                  # Additional documentation
    ├── architecture.md
    └── algorithm.md
```

## ⚙️ Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--video` | `required` | Input video file path |
| `--output` | `output.mp4` | Output video filename |
| `--model` | `yolov8n.pt` | YOLO model file (n/s/m/l/x) |
| `--line-position` | `0.5` | Counting line position (0-1) |
| `--confidence` | `0.5` | Detection confidence threshold (0-1) |
| `--classes` | `[2,3,5,7]` | Classes to detect |
| `--device` | `cuda:0` | Device (cuda:0 or cpu) |

### Model Options

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| yolov8n.pt | 6.2 MB | ⚡⚡⚡ | ⭐⭐ | Fast processing |
| yolov8s.pt | 21.5 MB | ⚡⚡ | ⭐⭐⭐ | Balanced |
| yolov8m.pt | 49.7 MB | ⚡ | ⭐⭐⭐⭐ | High accuracy |
| yolov8l.pt | 83.7 MB | 🐢 | ⭐⭐⭐⭐⭐ | Best accuracy |

## 🔬 Technical Details

### Data Processing Pipeline

#### 1. **Data Collection**
- Video formats: MP4, AVI, MOV
- Resolution: 720p - 4K
- FPS: 15-60

#### 2. **Data Normalization**
```python
# YOLO performs automatic normalization
- Images resized to 640x640
- Pixel values normalized to 0-1
- Aspect ratio preserved (with padding)
```

#### 3. **Classification**
COCO dataset classes:
- Class 2: Car
- Class 3: Motorcycle
- Class 5: Bus
- Class 7: Truck

#### 4. **Labeling**
- Uses YOLO pretrained model (COCO dataset)
- 80 different object categories
- Customizable with transfer learning

### Algorithm Complexity

- **Time Complexity**: O(n) - n: number of frames
- **Space Complexity**: O(m) - m: number of detected objects
- **FPS**: ~30-60 (with GPU), ~10-15 (with CPU)

## 🐛 Troubleshooting

### Video Won't Open

```python
# Check video path
import os
if not os.path.exists(video_path):
    print("Video not found!")
```

### GPU Not Found

```bash
# Use CPU instead
python vehicle_counter.py --video input.mp4 --device cpu
```

### Incorrect Counts

```python
# Adjust counting line position
counter = VehicleCounter(line_position=0.6)  # Lower position

# Or increase confidence threshold
results = model.track(frame, conf=0.6)
```

### Low FPS

```python
# Process every Nth frame
if frame_count % 2 != 0:  # Skip every 2nd frame
    continue
```

**Test Environment:**
- GPU: NVIDIA T4 COLAB GPU
- Model: YOLOv8n

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Ideas

- [ ] Multi-lane counting support
- [ ] Speed estimation
- [ ] Vehicle type classification
- [ ] Web interface
- [ ] Real-time streaming support
- [ ] Database integration
- [ ] API endpoints

## 📝 Changelog

### v1.0.0 (2025-01-10)
- ✨ Initial release
- 🎯 YOLOv8 integration
- 📊 Bidirectional counting
- 🎨 Visual output

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**[Your Name]**
- GitHub: [@username](https://github.com/username)
- Email: email@example.com
- LinkedIn: [profile-link](https://linkedin.com/in/profile)

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLOv8
- [OpenCV](https://opencv.org/) - Computer Vision library
- [PyTorch](https://pytorch.org/) - Deep Learning framework

## 📞 Contact

For questions:
- Open an issue: [GitHub Issues](https://github.com/username/vehicle-counter/issues)
- Discussions: [GitHub Discussions](https://github.com/username/vehicle-counter/discussions)

---

⭐ If you like this project, don't forget to give it a star!

**Made with ❤️ and Python**
