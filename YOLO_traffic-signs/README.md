# Traffic Sign Detection with YOLOv8

This project demonstrates an **end-to-end pipeline** for training a YOLOv8 model to detect traffic signs.
The workflow covers: **downloading a dataset from Roboflow (COCO format)**, converting it to YOLOv8 format, training on **Google Colab**, evaluating results, and analyzing improvements.

---

## 📂 Project Structure

```
traffic-sign-yolo/
├─ data/
│  ├─ images/{train,val,test}
│  └─ labels/{train,val,test}
├─ artifacts/
│  └─ best.pt
├─ runs/
│  └─ detect/train/   # training outputs (plots, logs, weights)
└─ data.yaml
```

---

## 🚦 Workflow

### 1. Dataset Preparation

* The dataset was downloaded from **Roboflow** in **COCO format**.
* COCO annotations (`x_min, y_min, width, height` in pixels) were converted into YOLOv8 format (`class_id, x_center, y_center, width, height` normalized to 0–1).
* Splits were organized into `train/`, `val/`, and `test/`.
* Category IDs from COCO were re-mapped to contiguous YOLO IDs (`0..N-1`).
* The **`valid` folder** from Roboflow was renamed to `val` to comply with YOLO’s expectations.

### 2. Format Conversion

* Each image receives a `.txt` file with annotations in YOLO format.
* Example (YOLO label):

  ```
  class_id x_center y_center width height
  ```
* This conversion step is critical: if labels are incorrect, the model cannot learn, no matter how many epochs are trained.

### 3. Training

* Training was conducted on **Google Colab with GPU (T4/A100)**.
* Model: **YOLOv8n (nano)** for fast prototyping.
* Key parameters:

  * `imgsz=640`
  * `epochs=50`
  * `optimizer=adamw` with `cos_lr=True`
  * `early stopping` with patience=15
* The **best model** according to validation performance was saved as `best.pt` in Google Drive.

### 4. Evaluation

* **Validation set** was used during training to select `best.pt`.
* **Test set** was used after training to measure final performance.
* Metrics:

  * **mAP\@50 ≈ 94%**
  * **mAP\@50–95 ≈ 79%**
* Strong classes: regulatory signs (e.g., *stop*, *do\_not\_enter*).
* Weaker classes: traffic light colors (*red/yellow/green*) due to visual similarity and small object size.

### 5. Results Analysis

* Training outputs include:

  * `results.png`: loss and mAP curves
  * `PR_curve.png`: precision-recall curves
  * `confusion_matrix.png`: per-class confusion
* Label visualization confirmed correct bounding boxes.
* Prediction visualization (`runs/detect/predict*`) showed good detection overall.

---

## 🔑 Train / Val / Test Explanation

* **Train**: Data used to optimize model weights.
* **Validation (val)**: Not used to update weights. Checked after each epoch to:

  * detect overfitting,
  * enable early stopping,
  * select the **best.pt** checkpoint.
* **Test**: Only used *after training* to report final model performance on unseen data.

---

## 📊 Results

* **Overall performance:**

  * mAP\@50 \~ 94%
  * mAP\@50–95 \~ 79%
* **Observations:**

  * Clear-shaped signs are easy to detect.
  * Similar color classes (traffic light states) confuse the model.

---

## 🚀 Possible Improvements

* **Dataset enhancements**:

  * Add more close-up samples of red/yellow lights.
  * Include varied conditions (night, rain, different camera angles).
  * Double-check label accuracy.

* **Training enhancements**:

  * Increase image size (`imgsz=768` or 832) to capture small objects.
  * Use larger models (`yolov8s`, `yolov8m`).
  * Train longer (`epochs=80–120`, early stopping prevents waste).
  * Use augmentation (mosaic, mixup, HSV color jitter, slight perspective).

* **Two-stage approach (optional)**:

  * Stage 1: Detect traffic lights.
  * Stage 2: Classify the cropped traffic light into *red/green/yellow*.

---

## 🙏 Acknowledgements

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [Roboflow](https://roboflow.com) for dataset hosting and export tools
* [Roboflow-Project](https://universe.roboflow.com/roboflow-100/road-signs-6ih4y/dataset/2)

---

✅ This README summarizes the **entire pipeline**: from dataset conversion to YOLO format, through training and validation, to results and future improvements.

👉 İstersen bunun başına **bir proje diyagramı (workflow image)** ekleyelim, GitHub README’de görsel olarak da hoş durur. İstiyor musun?
