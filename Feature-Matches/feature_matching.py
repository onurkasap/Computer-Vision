import cv2
import matplotlib.pyplot as plt
import numpy as np

# Görüntüleri yükleme (Kendi dosya adlarınızla değiştirin)
img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)  # Sorgu görüntüsü
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)  # Eğitim görüntüsü

# SIFT Dedektörünü Başlatma
sift = cv2.SIFT_create()

# Anahtar Noktaları ve Tanımlayıcıları Bulma
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Kaba Kuvvet Eşleştiriciyi Başlatma (Varsayılan olarak L2 mesafesi kullanır)
bf = cv2.BFMatcher()

# k-En Yakın Komşu (k=2) Eşleşmesini Bulma
# k=2: Her SIFT tanımlayıcısı için en yakın 2 komşuyu buluruz.
matches = bf.knnMatch(des1, des2, k=2)

# Lowe's Oran Testi Uygulama (Hatalı eşleşmeleri eleme)
# En yakın eşleşme, ikinci en yakın eşleşmeden çok daha iyi olmalıdır.
iyi_eslesmeler = []
for m, n in matches:
    # Eğer en yakın mesafe, ikinci en yakının %75'inden azsa, kabul et.
    if m.distance < 0.75 * n.distance:
        iyi_eslesmeler.append([m])

# Eşleşmeleri görselleştirme
img_eslesme = cv2.drawMatchesKnn(
    img1, kp1, img2, kp2, iyi_eslesmeler, None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Sonucu gösterme
plt.figure(figsize=(15, 8))
plt.imshow(img_eslesme)
plt.title("SIFT + Brute-Force (Oran Testli)")
plt.show()



#%%


import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)  # Sorgu görüntüsü
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)  # Eğitim görüntüsü


# ORB Dedektörünü Başlatma
orb = cv2.ORB_create(nfeatures=5000) # Daha fazla anahtar nokta deneyebiliriz

# Anahtar Noktaları ve Tanımlayıcıları Bulma
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Tanımlayıcıların float değil, ikili (binary) olduğundan emin olma
des1 = np.float32(des1) if des1.dtype != np.uint8 else des1
des2 = np.float32(des2) if des2.dtype != np.uint8 else des2

# Kaba Kuvvet Eşleştiriciyi Başlatma
# cv2.NORM_HAMMING: ORB gibi ikili tanımlayıcılar için kullanılır.
# crossCheck=True: Birinci setten A özniteliğinin en iyi eşleşmesi B ise VE
# İkinci setten B özniteliğinin en iyi eşleşmesi A ise eşleşmeyi kabul et.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Eşleşmeleri Bulma
matches = bf.match(des1, des2)

# Mesafeye göre sıralama (En iyi eşleşmeler en başta olacak)
matches = sorted(matches, key=lambda x: x.distance)

# En iyi 50 eşleşmeyi çizme
n_matches = 50
img_eslesme = cv2.drawMatches(
    img1, kp1, img2, kp2, matches[:n_matches], None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Sonucu gösterme
plt.figure(figsize=(15, 8))
plt.imshow(img_eslesme)
plt.title(f"ORB + Brute-Force (Hamming Mesafesi, İlk {n_matches} Eşleşme)")
plt.show()


#%%

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Görüntüleri yükleme
img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

# SIFT Dedektörünü Başlatma
sift = cv2.SIFT_create()

# Anahtar Noktaları ve Tanımlayıcıları Bulma
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Tanımlayıcıları float32'ye dönüştürme (FLANN için gereklidir)
des1 = np.float32(des1)
des2 = np.float32(des2)

# ----------------------------------------------------
# FLANN Parametreleri
# ----------------------------------------------------

# 1. Index Parametreleri (Algoritma Seçimi: KD-Tree)
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5) # 5 ağaç kullan

# 2. Arama Parametreleri
search_params = dict(checks=50) # Kontrol edilecek yaprak sayısı

# FLANN Eşleştiriciyi Başlatma
flann = cv2.FlannBasedMatcher(index_params, search_params)

# k-En Yakın Komşu (k=2) Eşleşmesini Bulma
matches = flann.knnMatch(des1, des2, k=2)

# Lowe's Oran Testi Uygulama (Hata elemesi)
iyi_eslesmeler = []
# Eşleşmeleri çizerken maske kullanacağız
matchesMask = [[0, 0] for i in range(len(matches))] 

for i, (m, n) in enumerate(matches):
    # m.distance < 0.7 * n.distance (Bu eşiği 0.7 yerine 0.75 de kullanabiliriz)
    if m.distance < 0.7 * n.distance:
        iyi_eslesmeler.append(m)
        matchesMask[i] = [1, 0] # Çizim için maske işaretleme

# Eşleşmeleri görselleştirme
draw_params = dict(
    matchColor=(0, 255, 0),       # Eşleşme çizgileri yeşil
    singlePointColor=(255, 0, 0), # Anahtar noktalar mavi
    matchesMask=matchesMask,      # Sadece maskelenen (iyi) eşleşmeleri çiz
    flags=cv2.DrawMatchesFlags_DEFAULT
)

img_eslesme = cv2.drawMatchesKnn(
    img1, kp1, img2, kp2, matches, None, **draw_params
)

# Sonucu gösterme
plt.figure(figsize=(15, 8))
plt.imshow(img_eslesme)
plt.title("SIFT + FLANN Eşleştirme (KD-Tree ve Oran Testi)")
plt.show()