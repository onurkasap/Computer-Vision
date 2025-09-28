# Feature Matching with OpenCV

This project demonstrates different feature matching techniques using OpenCV for computer vision applications. The implementation compares three different approaches: SIFT with Brute-Force matching, ORB with Brute-Force matching, and SIFT with FLANN-based matching.

## Project Structure

```
feature-matching/
├── feature_matching.py          # Main script with feature matching implementations
├── img1.jpg            # Query image (first image for comparison)
├── img2.jpg            # Training image (second image for comparison)
└── README.md           # This file
```

## Features

The project implements three distinct feature matching approaches:

### 1. SIFT + Brute-Force Matcher with Ratio Test
- Uses SIFT (Scale-Invariant Feature Transform) detector
- Applies Brute-Force matcher with k-nearest neighbors (k=2)
- Implements Lowe's ratio test to filter out poor matches
- Threshold: 0.75 ratio for match acceptance

### 2. ORB + Brute-Force Matcher with Cross-Check
- Uses ORB (Oriented FAST and Rotated BRIEF) detector
- Configurable feature count (default: 5000 features)
- Applies Hamming distance for binary descriptors
- Uses cross-check validation for robust matching
- Displays top 50 best matches

### 3. SIFT + FLANN Matcher with KD-Tree
- Uses SIFT detector with FLANN (Fast Library for Approximate Nearest Neighbors)
- Implements KD-Tree algorithm for efficient matching
- Applies Lowe's ratio test with 0.7 threshold
- Optimized for speed with large descriptor sets

## Requirements

```python
opencv-python>=4.5.0
matplotlib>=3.3.0
numpy>=1.19.0
```

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd feature-matching
```

2. Install required dependencies:
```bash
pip install opencv-python matplotlib numpy
```

3. Place your images:
   - Add your first image as `img1.jpg` (query image)
   - Add your second image as `img2.jpg` (training image)

## Usage

Run the script to see all three matching techniques:

```bash
python feature_matching.py
```

The script will display three visualization windows showing:
1. SIFT + Brute-Force matching results
2. ORB + Brute-Force matching results  
3. SIFT + FLANN matching results

## How It Works

### SIFT (Scale-Invariant Feature Transform)
- Detects keypoints that are invariant to scale and rotation
- Generates 128-dimensional feature descriptors
- Excellent for matching images with different scales or orientations

### ORB (Oriented FAST and Rotated BRIEF)
- Fast binary feature descriptor
- Rotation invariant and noise resistant
- Computationally efficient alternative to SIFT
- Uses Hamming distance for binary descriptor comparison

### Matching Strategies

**Brute-Force Matcher:**
- Compares each descriptor with all descriptors in the other set
- Guarantees finding the best match
- Slower but more accurate for smaller descriptor sets

**FLANN Matcher:**
- Uses approximate nearest neighbor search
- Significantly faster for large descriptor sets
- KD-Tree algorithm for efficient high-dimensional searches

**Lowe's Ratio Test:**
- Filters out ambiguous matches
- Compares distance to nearest vs second-nearest neighbor
- Accepts matches only if ratio is below threshold (0.7-0.75)

## Parameters You Can Adjust

### SIFT Parameters
- Number of features: Modify `cv2.SIFT_create()` parameters
- Ratio test threshold: Change `0.75` in ratio test condition

### ORB Parameters
- `nfeatures`: Number of features to detect (default: 5000)
- Number of displayed matches: Modify `n_matches` variable

### FLANN Parameters
- `trees`: Number of KD-trees (default: 5)
- `checks`: Number of leaf nodes to check (default: 50)
- Ratio threshold: Currently set to 0.7

## Expected Output

The script generates three matplotlib figures showing:
- Matched keypoints connected by lines
- Color-coded connections indicating match quality
- Title indicating the matching method used

## Tips for Better Results

1. **Image Quality**: Use high-resolution images with rich texture details
2. **Lighting**: Ensure consistent lighting conditions between images
3. **Overlap**: Images should have sufficient overlapping regions
4. **Parameter Tuning**: Adjust ratio test thresholds based on your specific use case

## Common Use Cases

- Image stitching and panorama creation
- Object recognition and tracking
- Visual SLAM (Simultaneous Localization and Mapping)
- Augmented reality applications
- Image registration and alignment

## Troubleshooting

**No matches found:**
- Check if images have sufficient texture and features
- Verify image file paths and formats
- Try adjusting ratio test thresholds

**Poor matching quality:**
- Increase number of features for ORB
- Adjust FLANN parameters for different image types
- Consider preprocessing images (contrast enhancement, etc.)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
