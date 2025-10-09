# 🚗 Araç Sayma Sistemi - YOLO ile Görüntü İşleme - Vehicle Counter System - Computer Vision with YOLO


YOLOv8 kullanarak videolardaki araçları tespit eden, takip eden ve gidiş-geliş yönlerine göre sayan yapay zeka destekli bir projedir.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![YOLO](https://img.shields.io/badge/YOLO-v8-red.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Demo](#-demo)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Nasıl Çalışır?](#-nasıl-çalışır)
- [Proje Yapısı](#-proje-yapısı)
- [Parametreler](#️-parametreler)
- [Teknik Detaylar](#-teknik-detaylar)
- [Sorun Giderme](#-sorun-giderme)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## ✨ Özellikler

- 🎯 **Gerçek Zamanlı Tespit**: YOLOv8 ile araç tespiti
- 🔢 **Nesne Takibi**: Her aracı benzersiz ID ile takip eder
- ↕️ **Yön Tespiti**: Gidiş ve geliş yönlerini otomatik algılar
- 📊 **Anlık Sayım**: Sağ üst köşede canlı istatistikler
- 🎨 **Görsel Çıktı**: Bounding box'lar ve ID etiketleri
- ⚡ **Hızlı İşleme**: GPU desteği ile optimize edilmiş
- 🎬 **Video İhracı**: İşlenmiş videoyu kaydetme

## 🎥 Demo

### Giriş Videosu
https://drive.google.com/file/d/1HE2tud2OjGnd0x_SxK9jlnNtXIx67jna/view?usp=sharing

### Çıkış Videosu
https://drive.google.com/file/d/1Amdmjj0pI8fSbzrkqN_NrHKSXZ9a8Iwr/view?usp=sharing

**Sonuçlar:**
- 🚗 Giden Araçlar: 98
- 🚙 Gelen Araçlar: 108
- 🔢 Toplam: 206

## 🚀 Kurulum

### Gereksinimler

```bash
Python 3.8+
CUDA 11.0+ (GPU kullanımı için, opsiyonel)
```

### Adım 1: Repository'yi Klonlayın

```bash
git clone https://github.com/kullaniciadi/vehicle-counter.git
cd vehicle-counter
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

### Adım 3: Gerekli Kütüphaneleri Yükleyin

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

### Adım 4: YOLO Modelini İndirin

Model otomatik olarak indirilecektir, ancak manuel indirmek isterseniz:

```bash
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

## 💻 Kullanım

### Google Colab'da Kullanım

1. Colab notebook'u açın: [Colab Link](#)
2. Kodu çalıştırın
3. Video dosyanızı yükleyin
4. İşlenmiş videoyu indirin

### Yerel Bilgisayarda Kullanım

```bash
python vehicle_counter.py --video path/to/video.mp4
```

### Parametreler ile Kullanım

```bash
python vehicle_counter.py \
    --video cars.mp4 \
    --output output_counted.mp4 \
    --line-position 0.5 \
    --model yolov8n.pt \
    --confidence 0.5
```

## 🧠 Nasıl Çalışır?

### 1. Video İşleme Akışı

```
Video Girişi → Frame Ayırma → YOLO Tespiti → Nesne Takibi → Sayım → Video Çıkışı
```

### 2. Sayım Algoritması

```python
# Her frame için:
1. YOLO ile araçları tespit et
2. Her araca benzersiz ID ata (tracking)
3. Bounding box'ın alt/üst kenarını kontrol et
4. Kenar sayım çizgisini geçti mi?
   - Yukarıdan aşağı → GIDEN +1
   - Aşağıdan yukarı → GELEN +1
5. Sayılan ID'leri kaydet (tekrar sayma yok)
```

### 3. Görsel Algoritma

```
Frame N-1:     Frame N:
  ┌────┐         
  │ 🚗 │       ┌────┐
  └────┘       │ 🚗 │  ← Alt kenar çizgiyi geçti
━━━━━━━━━━━━━  └────┘  ✅ SAYILDI!
              ━━━━━━━━━━━━━
```

## 📁 Proje Yapısı

```
vehicle-counter/
│
├── vehicle_counter.py      # Ana program
├── requirements.txt        # Bağımlılıklar
├── README.md              # Dokümantasyon
├── LICENSE                # Lisans
│
├── models/                # YOLO modelleri
│   └── yolov8n.pt
│
├── input/                 # Giriş videoları
│   └── sample_video.mp4
│
├── output/                # Çıkış videoları
│   └── output_counted.mp4
│
└── docs/                  # Ek dokümantasyon
    ├── architecture.md
    └── algorithm.md
```

## ⚙️ Parametreler

| Parametre | Varsayılan | Açıklama |
|-----------|-----------|----------|
| `--video` | `required` | Giriş video dosyası yolu |
| `--output` | `output.mp4` | Çıkış video dosyası adı |
| `--model` | `yolov8n.pt` | YOLO model dosyası (n/s/m/l/x) |
| `--line-position` | `0.5` | Sayım çizgisi konumu (0-1 arası) |
| `--confidence` | `0.5` | Tespit güven eşiği (0-1 arası) |
| `--classes` | `[2,3,5,7]` | Tespit edilecek sınıflar |
| `--device` | `cuda:0` | İşlemci (cuda:0 veya cpu) |

### Model Seçenekleri

| Model | Boyut | Hız | Doğruluk | Kullanım |
|-------|-------|-----|----------|----------|
| yolov8n.pt | 6.2 MB | ⚡⚡⚡ | ⭐⭐ | Hızlı işleme |
| yolov8s.pt | 21.5 MB | ⚡⚡ | ⭐⭐⭐ | Dengeli |
| yolov8m.pt | 49.7 MB | ⚡ | ⭐⭐⭐⭐ | Yüksek doğruluk |
| yolov8l.pt | 83.7 MB | 🐢 | ⭐⭐⭐⭐⭐ | En iyi doğruluk |

## 🔬 Teknik Detaylar

### Veri İşleme Pipeline

#### 1. **Veri Toplama**
- Video formatları: MP4, AVI, MOV
- Çözünürlük: 720p - 4K
- FPS: 15-60

#### 2. **Veri Normalizasyonu**
```python
# YOLO otomatik normalizasyon yapar
- Görüntüler 640x640'a yeniden boyutlandırılır
- Piksel değerleri 0-1 arasına normalize edilir
- Aspect ratio korunur (padding ile)
```

#### 3. **Sınıflandırma**
COCO dataset sınıfları:
- Class 2: Car (Araba)
- Class 3: Motorcycle (Motosiklet)
- Class 5: Bus (Otobüs)
- Class 7: Truck (Kamyon)

#### 4. **Etiketleme**
- YOLO pretrained model kullanılır (COCO dataset)
- 80 farklı nesne kategorisi
- Transfer learning ile özelleştirilebilir

### Algoritma Karmaşıklığı

- **Zaman Karmaşıklığı**: O(n) - n: frame sayısı
- **Alan Karmaşıklığı**: O(m) - m: tespit edilen nesne sayısı
- **FPS**: ~30-60 (GPU ile), ~10-15 (CPU ile)

## 🐛 Sorun Giderme

### Video Açılmıyor

```python
# Video yolunu kontrol edin
import os
if not os.path.exists(video_path):
    print("Video bulunamadı!")
```

### GPU Bulunamadı

```bash
# CPU kullanın
python vehicle_counter.py --video input.mp4 --device cpu
```

### Yanlış Sayımlar

```python
# Sayım çizgisi konumunu ayarlayın
counter = VehicleCounter(line_position=0.6)  # Daha aşağı

# Veya güven eşiğini artırın
results = model.track(frame, conf=0.6)
```

### Düşük FPS

```python
# Her N. frame'i işleyin
if frame_count % 2 != 0:  # Her 2. frame'i atla
    continue
```

## 📊 Performans



**Test Ortamı:**
- GPU: NVIDIA T4 COLAB1
- Model: YOLOv8n


## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

### Geliştirme Fikirleri

- [ ] Multi-lane sayım desteği
- [ ] Hız tahmini
- [ ] Araç tipi sınıflandırması
- [ ] Web arayüzü
- [ ] Real-time streaming desteği
- [ ] Database entegrasyonu
- [ ] API endpoint'leri

## 📝 Changelog

### v1.0.0 (2025-01-10)
- ✨ İlk sürüm
- 🎯 YOLOv8 entegrasyonu
- 📊 Gidiş-geliş sayımı
- 🎨 Görsel çıktı

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.


## 🙏 Teşekkürler

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLOv8
- [OpenCV](https://opencv.org/) - Computer Vision kütüphanesi
- [PyTorch](https://pytorch.org/) - Deep Learning framework

## 📞 İletişim

Sorularınız için:
- Issue açın: [GitHub Issues](https://github.com/kullaniciadi/vehicle-counter/issues)
- Tartışmalar: [GitHub Discussions](https://github.com/kullaniciadi/vehicle-counter/discussions)

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Made with ❤️ and Python**
