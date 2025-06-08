# 🚦 Sistem Prediksi Kemacetan Lalu Lintas Kota Bengkulu Berbasis Kecerdasan Buatan

## 1. 🤖 Model AI yang Digunakan

### Model 1: Long Short-Term Memory (LSTM)

* **Jenis Model:** Neural Network (Recurrent)
* **Kelebihan:**

  * Cocok untuk data deret waktu seperti jumlah kendaraan per jam, per hari, atau per minggu.
  * Mampu mengingat pola jangka panjang seperti jam sibuk dan musim liburan.
* **Kasus Penggunaan:**

  * Prediksi volume kendaraan dalam beberapa jam ke depan berdasarkan data historis.

### Model 2: Random Forest

* **Jenis Model:** Ensemble Classifier
* **Kelebihan:**

  * Menangani data dengan banyak fitur kategorikal dan numerik.
  * Tahan terhadap overfitting dan efektif pada data real-world yang noisy.
* **Kasus Penggunaan:**

  * Klasifikasi kemacetan (macet / tidak macet).
  * Penentuan rute optimal berdasarkan kombinasi fitur (cuaca, hari, waktu, volume kendaraan, dll).

## 2. 📊 Jenis dan Sumber Data

### Jenis Data yang Diperlukan:

| Jenis Data       | Deskripsi                                                          |
| ---------------- | ------------------------------------------------------------------ |
| Data Lalu Lintas | Volume kendaraan per jam di titik rawan macet                      |
| Data GPS         | Lokasi dan kecepatan kendaraan dari aplikasi navigasi              |
| Data Cuaca       | Curah hujan, suhu, dan visibilitas dari BMKG                       |
| Data Event Lokal | Hari libur nasional, festival kota, demo, atau event besar lainnya |
| Data Jalan       | Layout jalan, jumlah jalur, simpang, dan rambu (dari OSM)          |

### Sumber Data:

* **Dinas Perhubungan Bengkulu**: Kamera CCTV, loop detector, statistik lalu lintas.
* **API Navigasi (Google Maps, Waze)**: Kecepatan kendaraan, estimasi waktu tempuh.
* **BMKG**: API prakiraan dan data cuaca harian.
* **OpenStreetMap (OSM)**: Struktur jalan dan integrasi ke peta.
* **Simulasi Awal**: Data sintetik jika data asli belum tersedia.

### Proses Praproses Data:

* **Normalisasi**: Skala nilai numerik ke \[0–1].
* **Ekstraksi waktu**: Jam, hari, tanggal, akhir pekan, musim liburan.
* **Encoding**: Cuaca → one-hot / label encoding.
* **Imputasi**: Mengisi data hilang (interpolasi atau rata-rata).
* **Feature Engineering**: Kombinasi fitur untuk menghasilkan probabilitas kemacetan.

## 3. 🛠️ Desain Alur Sistem

### a. Diagram Arsitektur Sistem

```plaintext
     Sensor Lalu Lintas & Data GPS
                   │
     ┌─────────────▼─────────────┐
     │   Data Ingestion Service  │  (Streaming/API)
     └─────────────┬─────────────┘
                   ▼
     ┌─────────────────────────────┐
     │     Data Preprocessing      │  (Cleaning, Encoding, Normalisasi)
     └─────────────────────────────┘
                   ▼
     ┌─────────────────────────────┐
     │     Model AI (LSTM / RF)    │  (Training & Predicting)
     └─────────────────────────────┘
                   ▼
     ┌─────────────────────────────┐
     │   Sistem Rekomendasi Rute   │
     └─────────────────────────────┘
                   ▼
     ┌─────────────────────────────┐
     │   Antarmuka (Web / Mobile)  │
     └─────────────────────────────┘
```

### b. Narasi Teknis Sistem

1. Sistem mengambil data real-time dari sensor lalu lintas, GPS kendaraan, dan API cuaca.
2. Data dikumpulkan oleh Ingestion Layer dan kemudian dibersihkan dan diproses.
3. Model AI:

   * **LSTM** → Prediksi volume kendaraan untuk jam berikutnya.
   * **Random Forest** → Prediksi titik rawan kemacetan.
4. Hasil prediksi digunakan untuk merekomendasikan rute tercepat.
5. Output ditampilkan kepada pengguna dalam bentuk peringatan dan peta rute.


## 4. ✅ Strategi Evaluasi Model

### Validasi dan Pengujian

| Model             | Validasi                     | Tujuan                                            |
| ----------------- | ---------------------------- | ------------------------------------------------- |
| **LSTM**          | Time Series Cross-Validation | Validasi berurutan untuk menghindari data leakage |
| **Random Forest** | K-Fold Cross Validation      | Evaluasi akurasi dengan data acak                 |

### Metrik Evaluasi

| Metrik               | Fungsi                                   |
| -------------------- | ---------------------------------------- |
| **MAE**              | Evaluasi error prediksi volume kendaraan |
| **RMSE**             | Alternatif pengukuran error              |
| **Accuracy**         | Akurasi klasifikasi macet/tidak          |
| **F1-score**         | Keseimbangan precision dan recall        |
| **Confusion Matrix** | Distribusi kesalahan prediksi            |

## 5. 🚀 Pengembangan Lanjutan

| Fitur Tambahan                 | Manfaat                                      |
| ------------------------------ | -------------------------------------------- |
| **Integrasi IoT**              | Data lalu lintas lebih real-time dan presisi |
| **Push Notifikasi**            | Memberi peringatan otomatis ke pengguna      |
| **Dashboard Admin**            | Monitoring kemacetan dan laporan statistik   |
| **Prediksi Musiman**           | Antisipasi kemacetan saat libur Lebaran      |
| **Navigasi Transportasi Umum** | Rekomendasi angkot/bus sebagai alternatif    |

Cek Situsnya : https://ammar3544.github.io/ModelAI/prediksi_kemacetan.html
