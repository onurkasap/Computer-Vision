
# Street Basketball Object Detection with YOLOv11

Bu proje, sokak basketbolu görüntülerinde top, potaya ve oyunculara yönelik nesne tespiti yapmak için YOLOv11n modelini kullanmaktadır.

## 📋 Proje Özeti

YOLOv11n (nano) modeli kullanılarak streetball videolarından çıkarılan görüntüler üzerinde nesne tespiti gerçekleştirilmiştir. Model, basketbol topu, pota ve oyuncuları tespit edebilmektedir.

## 🎯 Tespit Edilen Sınıflar

- **Ball** (Top)
- **Hoop** (Pota)
- **Player** (Oyuncu)

## 📊 Veri Seti

### Veri Toplama
- 3 farklı streetball videosundan **102 görüntü** çıkarıldı
- **Roboflow** platformu kullanılarak manuel etiketleme yapıldı
- Data augmentation teknikleri uygulanarak **244 görüntüye** çıkarıldı

### Roboflow Veri Seti
🔗 [Roboflow Dataset Link]() 
> *Veri seti linkini buraya ekleyebilirsiniz*

## 🛠️ Kullanılan Teknolojiler

- **YOLOv11n** - Nesne tespit modeli
- **OpenCV** - Görüntü işleme (`imread`, `imshow`)
- **Roboflow** - Veri etiketleme ve augmentation
- **Google Colab** - Model eğitimi

## 🚀 Kullanım

### Gereksinimler
```bash
pip install ultralytics opencv-python
```

### Model Eğitimi
```python
from ultralytics import YOLO

# Model yükleme
model = YOLO('yolo11n.pt')

# Eğitim
results = model.train(data='data.yaml', epochs=50, imgsz=640)
```

### Tahmin
```python
import cv2

# Görüntü yükleme
img = cv2.imread('test_image.jpg')

# Tahmin
results = model.predict(img)

# Sonuçları gösterme
cv2.imshow('Detection', results[0].plot())
cv2.waitKey(0)
```

## 📸 Sonuçlar

Proje başarıyla streetball görüntülerinde top, pota ve oyuncu tespiti yapmaktadır. Model, gerçek zamanlı uygulamalar için yeterli hız ve doğruluk sunmaktadır.

### Örnek Çıktılar
Notebook içerisinde 2 adet örnek tespit sonucu bulunmaktadır.

## 📝 Notlar

- YOLOv11n modeli, düşük hesaplama gücü gerektiren hafif bir modeldir
- Gerçek zamanlı tespit için ideal performans sağlar
- Augmentation sayesinde model genelleme yeteneği artırılmıştır

## 🔗 Bağlantılar

- [Google Colab Notebook](https://github.com/onurkasap/Computer-Vision/blob/main/street_basketball_YOLOv11_ObjDet.ipynb)
- [YOLOv11 Documentation](https://docs.ultralytics.com/)

## 👤 Geliştirici

**Onur Kasap**
- GitHub: [@onurkasap](https://github.com/onurkasap)

---

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!
```
