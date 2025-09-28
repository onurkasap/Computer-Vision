# Feature Matching with OpenCV  

This project demonstrates different feature matching techniques in computer vision using **OpenCV** and **Python**.  
The goal is to detect keypoints between two images (`img1.jpg` and `img2.jpg`) and match them using different algorithms.  

## 📂 Files  
- `matching.py` → Contains the implementations for feature detection and matching.  
- `img1.jpg` → Query image.  
- `img2.jpg` → Training image.  

## 🔑 Implemented Methods  

### 1. **SIFT + Brute-Force (with Ratio Test)**  
- Uses the **SIFT (Scale-Invariant Feature Transform)** detector.  
- Matches descriptors with a Brute-Force matcher.  
- Applies **Lowe’s ratio test** to filter out poor matches.  

### 2. **ORB + Brute-Force (Hamming Distance)**  
- Uses the **ORB (Oriented FAST and Rotated BRIEF)** detector.  
- Descriptors are matched with **Hamming distance**.  
- Displays the **top-N matches** sorted by distance.  

### 3. **SIFT + FLANN (KD-Tree Search + Ratio Test)**  
- Uses **FLANN (Fast Library for Approximate Nearest Neighbors)** for efficient matching.  
- Applies KD-Tree for indexing and nearest-neighbor search.  
- Employs Lowe’s ratio test to remove incorrect matches.  

## 📊 Visualization  
Each method visualizes the matches between the two images using `matplotlib`.  
Examples include lines drawn between matched keypoints.  

## 🚀 Requirements  
- Python 3.8+  
- OpenCV (`cv2`)  
- NumPy  
- Matplotlib  

Install the dependencies with:  

```bash
pip install opencv-python numpy matplotlib
