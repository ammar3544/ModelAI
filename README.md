Sistem Prediksi Kemacetan Lalu Lintas Kota Bengkulu Berbasis Kecerdasan Buatan

1. Model AI yang Digunakan
Model 1: Long Short-Term Memory (LSTM)
•	Jenis Model: Neural Network (Recurrent)
•	Kelebihan:
o	Cocok untuk data deret waktu (time series) seperti jumlah kendaraan per jam, per hari, atau per minggu.
o	Mampu mengingat pola jangka panjang yang umum terjadi, seperti jam sibuk (rush hour) dan musim liburan.
•	Kasus Penggunaan:
o	Prediksi volume kendaraan dalam beberapa jam ke depan berdasarkan data historis.
Model 2: Random Forest
•	Jenis Model: Ensemble Classifier
•	Kelebihan:
o	Mampu menangani data dengan banyak fitur kategorikal dan numerik.
o	Tahan terhadap overfitting dan bekerja baik pada data real-world yang noisy.
•	Kasus Penggunaan:
o	Klasifikasi kemacetan (macet / tidak macet).
o	Membuat keputusan rute optimal berdasarkan kombinasi fitur (cuaca, hari, waktu, jumlah kendaraan, dll).












2. Jenis dan Sumber Data
 Jenis Data yang Diperlukan:
Jenis Data	Deskripsi
Data Lalu Lintas	Volume kendaraan per jam di tiap titik rawan macet
Data GPS	Lokasi dan kecepatan kendaraan dari pengguna aplikasi navigasi
Data Cuaca	Curah hujan, suhu, dan visibilitas dari BMKG
Data Event Lokal	Hari libur nasional, festival kota, demo, atau event besar lainnya
Data Jalan	Layout jalan, jumlah jalur, simpang, dan rambu (dari OSM)


 Sumber Data:
•	Dinas Perhubungan Bengkulu: Data kamera CCTV, loop detector, dan statistik lalu lintas.
•	API Navigasi (Google Maps, Waze): Kecepatan rata-rata kendaraan, estimasi waktu tempuh.
•	BMKG (cuaca.bmkg.go.id): API prakiraan dan data cuaca harian di Bengkulu.
•	OpenStreetMap: Untuk struktur jalan dan integrasi ke rute navigasi.
•	Simulasi Awal: Data sintetik jika sumber asli belum tersedia (bisa digenerate secara semi-otomatis).
Proses Praproses Data:
•	Normalisasi: Mengubah nilai numerik menjadi skala [0-1] (misalnya volume kendaraan, suhu).
•	Ekstraksi waktu: Jam, hari, tanggal, akhir pekan, musim liburan.
•	Encoding: Cuaca diubah ke numerik (One-hot atau Label Encoding).
•	Imputasi: Mengisi data hilang dengan interpolasi atau rata-rata bergerak.
•	Feature Engineering: Kombinasi fitur (cuaca + volume kendaraan + waktu) → probabilitas kemacetan.






3. Desain Alur Sistem
a. Diagram Arsitektur Sistem
scss
CopyEdit
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
     │        Model AI (LSTM / RF) │  (Training & Predicting)
     └─────────────────────────────┘
                   ▼
     ┌─────────────────────────────┐
     │  Sistem Rekomendasi Rute    │
     └─────────────────────────────┘
                   ▼
     ┌─────────────────────────────┐
     │   Antarmuka (Web / Mobile)  │
     └─────────────────────────────┘









b. Narasi Teknis Sistem
1.	Sistem mengambil data real-time dari sensor lalu lintas, GPS kendaraan, dan API cuaca.
2.	Data dikumpulkan oleh Ingestion Layer lalu dibersihkan dan diolah.
3.	Model AI:
o	LSTM untuk memprediksi volume kendaraan pada jam berikutnya.
o	Random Forest untuk menentukan kemungkinan titik rawan macet.
4.	Hasil prediksi dianalisis untuk merekomendasikan rute tercepat.
5.	Output sistem dikirim ke antarmuka pengguna (user) berupa peringatan dan peta rute.
























4.  Strategi Evaluasi Model
Validasi dan Pengujian
Model	Validasi	Tujuan
LSTM	Time Series Cross-Validation	Validasi berurutan untuk menghindari data leakage
Random Forest	K-Fold Cross Validation	Membagi data secara acak untuk evaluasi akurasi



Metrik Evaluasi
Metrik	Fungsi
MAE	Evaluasi error prediksi volume kendaraan
RMSE	Alternatif untuk mengukur error
Accuracy	Kemampuan klasifikasi benar (macet/tidak)
F1-score	Menyeimbangkan precision dan recall
Confusion Matrix	Menunjukkan distribusi kesalahan prediksi
________________________________________
5. Pengembangan Lanjutan
Fitur Tambahan	Manfaat
Integrasi IoT (kamera/sensor)	Data lalu lintas lebih real-time dan presisi
Push Notifikasi (Web/App)	Memberi peringatan otomatis ke pengguna jika terjadi potensi kemacetan
Dashboard Admin Pemerintah	Monitoring area kemacetan dan laporan statistik harian/mingguan
Prediksi Musiman (Libur Lebaran)	Membantu antisipasi peningkatan lalu lintas musiman
Navigasi Transportasi Umum	Rekomendasi angkot/bus sebagai alternatif transportasi

