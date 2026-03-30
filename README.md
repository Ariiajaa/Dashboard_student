# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang baik. Namun, institusi ini masih menghadapi tantangan besar dalam menjaga keberlangsungan studi mahasiswanya hingga selesai.

Kondisi ini berdampak langsung pada kualitas dan reputasi institusi, efisiensi penggunaan sumber daya pendidikan, serta hilangnya potensi kontribusi lulusan bagi masyarakat. Oleh karena itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data untuk mendeteksi mahasiswa berisiko sedini mungkin agar dapat dilakukan intervensi yang tepat dan tepat waktu.

### Permasalahan Bisnis

1. **Tingginya angka mahasiswa yang tidak menyelesaikan studi** — Institusi menghadapi tantangan serius berupa banyaknya mahasiswa yang keluar sebelum menyelesaikan pendidikan mereka, yang berdampak pada kualitas dan reputasi institusi secara keseluruhan.
2. **Tidak adanya sistem deteksi dini** — Institusi belum memiliki mekanisme yang memadai untuk mengidentifikasi mahasiswa yang berpotensi tidak menyelesaikan studi sebelum kondisi tersebut benar-benar terjadi.
3. **Kurangnya pemantauan berbasis data** — Departemen akademik belum memiliki alat yang cukup untuk memantau kondisi dan perkembangan mahasiswa secara menyeluruh dan berkelanjutan.
4. **Pengambilan keputusan yang belum proaktif** — Intervensi yang dilakukan selama ini masih bersifat reaktif, sehingga penanganan terhadap mahasiswa bermasalah seringkali terlambat dilakukan.

### Cakupan Proyek

1. **Data Understanding** — Eksplorasi dataset mahasiswa, pemeriksaan missing value, dan pemahaman distribusi data.
2. **Exploratory Data Analysis (EDA)** — Analisis mendalam: EDA univariate, multivariate, analisis korelasi, dan identifikasi pola dropout.
3. **Data Preparation** — Filter dataset, label encoding, pemisahan fitur-target, train-test split, dan pipeline preprocessing.
4. **Modeling** — Pembuatan model **binary classifier** (Dropout vs Graduate) menggunakan Random Forest Classifier. Data Enrolled tidak diikutsertakan dalam training karena belum memiliki label akhir.
5. **Evaluation** — Evaluasi model dengan Accuracy, ROC-AUC, Classification Report, dan Confusion Matrix.
6. **Business Dashboard** — Dashboard interaktif Metabase terhubung PostgreSQL (Supabase) untuk monitoring performa mahasiswa.
7. **Deployment** — Prototype machine learning menggunakan Streamlit yang dapat diakses secara online.

### Persiapan

Sumber data: [Predict students' dropout and academic success — UCI ML Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

---

## Struktur Folder Proyek

```
jaya-jaya-institut/
│
├── notebook.ipynb          # Notebook analisis lengkap (EDA, modeling, evaluation)
├── app.py                  # Prototype Streamlit
├── retrain.py              # Script retrain model (jalankan sebelum app.py)
├── data.csv                # Dataset mahasiswa (separator: semicolon)
│
├── model_student.pkl       # Model Random Forest (dihasilkan oleh retrain.py)
├── label_encoder.pkl       # Label encoder target (dihasilkan oleh retrain.py)
│
└── requirements.txt        # Dependencies Python
```

---

## Langkah-langkah Menjalankan Proyek

### Step 1 — Clone / Siapkan Folder Proyek

Pastikan semua file berikut sudah ada dalam satu folder:

- `notebook.ipynb`
- `app.py`
- `retrain.py`
- `data.csv`
- `requirements.txt`

### Step 2 — Buat Virtual Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```
streamlit
pandas
numpy
scikit-learn
joblib
```

> **Catatan**: Tidak perlu pin versi spesifik. Script `retrain.py` akan menyesuaikan model dengan versi sklearn yang terinstall di environment

### Step 4 — Jalankan Notebook Analisis

```bash
jupyter notebook notebook.ipynb
```

Jalankan semua cell dari atas ke bawah. Notebook ini mencakup:

- Data Understanding & pemeriksaan missing value
- Exploratory Data Analysis (EDA) lengkap
- Data Preparation: filter dataset (hanya Dropout & Graduate), encoding, split, pipeline
- Modeling & training Random Forest (binary classifier)
- Evaluation (Accuracy, ROC-AUC, Classification Report, Confusion Matrix)
- Inferensi data Enrolled untuk prediksi status akhir mahasiswa aktif

### Step 5 — Retrain Model (Wajib dilakukan sekali)

> ⚠️ **Penting**: Langkah ini wajib dilakukan agar model kompatibel dengan versi scikit-learn yang terinstall. Jika dilewati, Streamlit app akan error saat prediksi.

```bash
python retrain.py
```

Output yang diharapkan:

```
Training model (Binary: Dropout vs Graduate)...
✅ Model berhasil disimpan!
   scikit-learn version : x.x.x
   Classes              : ['Dropout' 'Graduate']  (Binary)
   File                 : model_student.pkl, label_encoder.pkl
```

Setelah step ini, dua file berikut akan dibuat/diperbarui:

- `model_student.pkl`
- `label_encoder.pkl`

### Step 6 — Jalankan Streamlit App (Lokal)

```bash
streamlit run app.py
```

Buka browser dan akses: `http://localhost:8501`

### Step 7 — Setup Business Dashboard (Metabase)

```bash
# Pull dan jalankan Metabase via Docker
docker pull metabase/metabase
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

Buka browser dan akses: `http://localhost:3000`

Login dengan:

```
Email    : aridp12367@gmail.com
Password : ari_Kuyy721
```

Kemudian:

1. Hubungkan Metabase ke database PostgreSQL (Supabase)
2. Upload `data.csv` ke Supabase sebagai tabel
3. Buat questions dan dashboard sesuai panduan di bawah

### Step 8 — Deploy ke Streamlit Community Cloud (Opsional)

```bash
# Inisialisasi git repository
git init
git add .
git commit -m "student dropout predictor"
git branch -M main
git remote add origin https://github.com/Ariiajaa/Dashboard_student.git
git push -u origin main
```

Kemudian:

1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Login dengan akun GitHub
3. Klik **New app**
4. Pilih repository, branch `main`, main file `app.py`
5. Klik **Deploy**

🔗 **Link Streamlit App**: https://jaya-jaya-institut-dropout-predictor.streamlit.app

---

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** yang terhubung dengan database **PostgreSQL pada Supabase**. Dashboard ini dirancang untuk membantu tim akademik Jaya Jaya Institut memahami distribusi dan faktor-faktor yang mempengaruhi status mahasiswa, dengan semua label ditampilkan secara kategorikal agar mudah dipahami.

**Visualisasi yang tersedia:**

| No  | Visualisasi                           | Jenis Chart      | Tujuan                                                          |
| --- | ------------------------------------- | ---------------- | --------------------------------------------------------------- |
| 1   | Total Mahasiswa                       | KPI Card         | Overview jumlah mahasiswa                                       |
| 2   | Total Dropout                         | KPI Card         | Jumlah mahasiswa yang dropout                                   |
| 3   | Total Graduate                        | KPI Card         | Jumlah mahasiswa yang lulus                                     |
| 4   | Dropout Rate (%)                      | KPI Card         | Persentase dropout keseluruhan                                  |
| 5   | Distribusi Status                     | Pie Chart        | Proporsi Graduate / Enrolled / Dropout                          |
| 6   | Dropout Rate by Tuition Fees          | Bar Chart        | Pengaruh pembayaran UKT (Tepat Waktu / Tidak Tepat Waktu)       |
| 7   | Status by Scholarship                 | Stacked Bar      | Pengaruh beasiswa (Pemegang Beasiswa / Bukan Pemegang Beasiswa) |
| 8   | Status by Debtor                      | Stacked Bar      | Pengaruh tunggakan (Memiliki Tunggakan / Tidak Ada Tunggakan)   |
| 9   | Rata-rata Nilai Sem 1 & 2 per Status  | Grouped Bar      | Performa akademik per status                                    |
| 10  | Rata-rata Unit Disetujui per Status   | Grouped Bar      | Jumlah SKS lulus per status                                     |
| 11  | Dropout Rate by Gender                | Bar Chart        | Perbandingan dropout (Laki-laki / Perempuan)                    |
| 12  | Rata-rata Usia Pendaftaran per Status | Bar Chart        | Pola usia mahasiswa per status                                  |
| 13  | Dropout Rate by Course (Top 10)       | Horizontal Bar   | Program studi dengan dropout tertinggi                          |
| 14  | Status by Waktu Kuliah                | Stacked Bar 100% | Pengaruh waktu kuliah (Kelas Siang / Kelas Malam)               |
| 15  | Rata-rata Admission Grade per Status  | Bar Chart        | Nilai masuk vs status kelulusan                                 |

> **Catatan**: Semua kolom binary (0/1) ditampilkan dengan label kategorikal yang deskriptif menggunakan `CASE WHEN` pada query SQL, sehingga visualisasi lebih mudah dipahami oleh pengguna non-teknis.

**Akses Dashboard:**

```
Email    : aridp12367@gmail.com
Password : ari_Kuyy721
```

---

## Conclusion

Berdasarkan seluruh proses analisis data dan pemodelan machine learning yang telah dilakukan:

1. **Jaya Jaya Institut menghadapi tantangan serius** terkait tingginya mahasiswa yang tidak menyelesaikan studi mereka, yang berdampak pada kualitas institusi dan efisiensi sumber daya pendidikan.

2. **Faktor-faktor utama yang mempengaruhi dropout** berdasarkan feature importance model dan EDA:
   - **Tuition_fees_up_to_date** — mahasiswa yang tidak membayar UKT tepat waktu memiliki risiko dropout yang sangat tinggi.
   - **Curricular_units_2nd_sem_approved** — jumlah unit lulus Semester 2 adalah prediktor terkuat; mahasiswa dropout hampir tidak lulus satupun unit.
   - **Curricular_units_1st_sem_approved** — pola yang sama terjadi di Semester 1.
   - **Nilai Semester 1 & 2** — nilai akademik mahasiswa dropout jauh di bawah mahasiswa yang lulus.
   - **Debtor** — mahasiswa yang memiliki tunggakan pembayaran memiliki risiko dropout lebih tinggi.
   - **Age_at_enrollment** — mahasiswa yang lebih tua saat mendaftar cenderung lebih banyak dropout.
   - **Scholarship_holder** — pemegang beasiswa memiliki tingkat kelulusan yang lebih baik.
   - **Admission_grade** — nilai masuk yang lebih tinggi berkorelasi positif dengan kelulusan.

3. **Model Random Forest Classifier (Binary: Dropout vs Graduate)** berhasil memprediksi status mahasiswa dengan performa yang sangat baik:
   - **Accuracy**: 91.2% — meningkat signifikan dibanding model multiclass sebelumnya.
   - **ROC-AUC**: 0.9566 — model sangat baik dalam membedakan mahasiswa yang akan dropout vs graduate.
   - **Dropout Precision**: 95% — sangat sedikit false positive dalam deteksi dropout.
   - **Graduate Recall**: 98% — hampir semua mahasiswa yang akan lulus teridentifikasi dengan benar.

4. **Inferensi mahasiswa Enrolled** menunjukkan dari mahasiswa yang masih aktif, sebagian diprediksi berisiko dropout dan perlu mendapat perhatian segera dari tim akademik.

5. **Business dashboard Metabase** berhasil dibuat dengan 15 visualisasi dan label kategorikal yang deskriptif untuk monitoring status dan performa mahasiswa secara real-time.

6. **Prototype Streamlit** berhasil dibuat dan dapat digunakan tim akademik untuk prediksi risiko dropout mahasiswa secara individual dan real-time.

### Rekomendasi Action Items

- **Pantau pembayaran UKT secara aktif** — segera lakukan outreach kepada mahasiswa yang terlambat membayar karena ini adalah prediktor dropout terkuat. Tawarkan opsi cicilan atau bantuan finansial kepada mahasiswa yang membutuhkan.
- **Buat sistem early warning berbasis performa Semester 1** — mahasiswa dengan jumlah unit lulus yang sangat rendah di Semester 1 harus segera didampingi oleh konselor akademik sebelum kondisinya semakin memburuk di Semester 2.
- **Perluas program beasiswa** — data menunjukkan pemegang beasiswa memiliki tingkat kelulusan yang lebih baik. Perluasan program beasiswa dapat menjadi investasi jangka panjang untuk meningkatkan angka kelulusan institusi.
- **Intervensi khusus untuk mahasiswa dengan profil risiko tinggi** — mahasiswa yang mendaftar di usia lebih tua dan memiliki kendala finansial membutuhkan program dukungan yang lebih fleksibel, seperti jadwal kuliah yang adaptif atau konseling karir.
- **Gunakan prototype Streamlit sebagai alat kerja tim akademik** — staf dapat memasukkan data mahasiswa untuk mendapatkan prediksi risiko dropout secara real-time dan mengambil tindakan preventif sebelum mahasiswa benar-benar keluar.
- **Evaluasi kurikulum program studi dengan tingkat putus studi tinggi** — analisis dashboard per program studi dapat mengidentifikasi program mana yang membutuhkan evaluasi kurikulum, perbaikan metode pengajaran, atau dukungan akademik tambahan.
