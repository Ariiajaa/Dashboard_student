# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang baik. Namun, institusi ini masih menghadapi tantangan besar, yaitu tingginya jumlah mahasiswa yang tidak menyelesaikan pendidikan mereka (dropout).

Tingginya angka dropout berdampak pada reputasi institusi, efisiensi penggunaan sumber daya pendidikan, dan hilangnya potensi kontribusi lulusan terhadap masyarakat. Oleh karena itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data untuk mendeteksi mahasiswa berisiko dropout sedini mungkin agar dapat dilakukan intervensi yang tepat.

### Permasalahan Bisnis

1. **Tingginya angka dropout mahasiswa** — Sekitar 32% mahasiswa tidak menyelesaikan studi mereka, jauh di atas angka ideal untuk institusi pendidikan berkualitas.
2. **Tidak adanya sistem deteksi dini** — Institusi belum memiliki mekanisme untuk mengidentifikasi mahasiswa berisiko dropout sebelum mereka benar-benar keluar.
3. **Kurangnya pemantauan berbasis data** — Departemen akademik belum memiliki dashboard untuk memonitor performa dan status mahasiswa secara real-time.
4. **Pengambilan keputusan kurang terarah** — Intervensi akademik selama ini bersifat reaktif, bukan proaktif berdasarkan pola data historis.

### Cakupan Proyek

1. **Data Understanding** — Eksplorasi dataset mahasiswa, pemeriksaan missing value, dan pemahaman distribusi data.
2. **Exploratory Data Analysis (EDA)** — Analisis mendalam: EDA univariate, multivariate, analisis korelasi, dan identifikasi pola dropout.
3. **Data Preparation** — Label encoding, pemisahan fitur-target, train-test split, dan pipeline preprocessing.
4. **Modeling** — Pembuatan model Random Forest Classifier untuk prediksi status mahasiswa (Dropout/Enrolled/Graduate).
5. **Evaluation** — Evaluasi model dengan Accuracy, Classification Report, dan Confusion Matrix.
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

> **Catatan**: Tidak perlu pin versi spesifik. Script `retrain.py` akan menyesuaikan model dengan versi sklearn yang terinstall di environment kamu.

### Step 4 — Jalankan Notebook Analisis

```bash
jupyter notebook notebook.ipynb
```

Jalankan semua cell dari atas ke bawah. Notebook ini mencakup:

- Data Understanding & pemeriksaan missing value
- Exploratory Data Analysis (EDA) lengkap
- Data Preparation & preprocessing pipeline
- Modeling & training Random Forest
- Evaluation (Accuracy, Classification Report, Confusion Matrix)

### Step 5 — Retrain Model (Tambahan file model)

> ⚠️ **Penting**: Tambahan agar model kompatibel dengan versi scikit-learn yang terinstall.

```bash
python retrain.py
```

Output yang diharapkan:

```
Training model...
✅ Model berhasil disimpan!
   sklearn version: x.x.x
   Classes: ['Dropout' 'Enrolled' 'Graduate']
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
Password : @kuy_ari639
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
git remote add origin https://github.com/Ariiajaa/Dashboard_student
git push -u origin main
```

Kemudian:

1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Login dengan akun GitHub
3. Klik **New app**
4. Pilih repository, branch `main`, main file `app.py`
5. Klik **Deploy**

🔗 **Link Streamlit App**: https://dashboardstudent-gjplmoxlbg2rpcaqhpxdru.streamlit.app/

---

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** yang terhubung dengan database **PostgreSQL pada Supabase**. Dashboard ini dirancang untuk membantu tim akademik Jaya Jaya Institut memahami distribusi dan faktor-faktor yang mempengaruhi status mahasiswa.

**Visualisasi yang tersedia:**

| No  | Visualisasi                           | Jenis Chart      | Tujuan                                   |
| --- | ------------------------------------- | ---------------- | ---------------------------------------- |
| 1   | Total Mahasiswa                       | KPI Card         | Overview jumlah mahasiswa                |
| 2   | Total Dropout                         | KPI Card         | Jumlah mahasiswa yang dropout            |
| 3   | Total Graduate                        | KPI Card         | Jumlah mahasiswa yang lulus              |
| 4   | Dropout Rate (%)                      | KPI Card         | Persentase dropout keseluruhan           |
| 5   | Distribusi Status                     | Pie Chart        | Proporsi Graduate / Enrolled / Dropout   |
| 6   | Dropout Rate by Tuition Fees          | Bar Chart        | Pengaruh pembayaran UKT terhadap dropout |
| 7   | Status by Scholarship                 | Stacked Bar      | Pengaruh beasiswa terhadap status        |
| 8   | Status by Debtor                      | Stacked Bar      | Pengaruh tunggakan terhadap dropout      |
| 9   | Rata-rata Nilai Sem 1 & 2 per Status  | Grouped Bar      | Performa akademik per status             |
| 10  | Rata-rata Unit Disetujui per Status   | Grouped Bar      | Jumlah SKS lulus per status              |
| 11  | Dropout Rate by Gender                | Bar Chart        | Perbandingan dropout berdasarkan gender  |
| 12  | Rata-rata Usia Pendaftaran per Status | Bar Chart        | Pola usia mahasiswa per status           |
| 13  | Dropout Rate by Course (Top 10)       | Horizontal Bar   | Program studi dengan dropout tertinggi   |
| 14  | Status by Waktu Kuliah                | Stacked Bar 100% | Pengaruh waktu kuliah terhadap status    |
| 15  | Rata-rata Admission Grade per Status  | Bar Chart        | Nilai masuk vs status kelulusan          |

**Akses Dashboard:**

```
Email    : aridp12367@gmail.com
Password : @kuy_ari639
```

---

## Conclusion

Berdasarkan seluruh proses analisis data dan pemodelan machine learning yang telah dilakukan:

1. **Angka dropout Jaya Jaya Institut mencapai ~32%** dari total 4.424 mahasiswa — angka yang cukup tinggi dan membutuhkan penanganan serius.

2. **Faktor-faktor utama yang mempengaruhi dropout** berdasarkan feature importance model dan EDA:
   - **Tuition_fees_up_to_date** — mahasiswa yang tidak membayar UKT tepat waktu memiliki dropout rate >80%.
   - **Curricular_units_2nd_sem_approved** — jumlah unit lulus Semester 2 adalah prediktor terkuat; mahasiswa dropout hampir tidak lulus satupun unit.
   - **Curricular_units_1st_sem_approved** — pola yang sama terjadi di Semester 1.
   - **Nilai Semester 1 & 2** — nilai akademik Dropout mendekati 0, jauh di bawah Graduate.
   - **Debtor** — mahasiswa penunggak memiliki risiko dropout lebih tinggi.
   - **Age_at_enrollment** — mahasiswa yang lebih tua saat mendaftar cenderung lebih banyak dropout.
   - **Scholarship_holder** — pemegang beasiswa memiliki tingkat kelulusan lebih tinggi.
   - **Admission_grade** — nilai masuk yang lebih tinggi berkorelasi dengan kelulusan.

3. **Model Random Forest Classifier** berhasil memprediksi status mahasiswa dengan:
   - **Accuracy**: 76.8%
   - **Dropout Precision**: 82% — model dapat mendeteksi mahasiswa berisiko dengan cukup akurat.
   - **Graduate Recall**: 93% — mahasiswa yang akan lulus hampir selalu teridentifikasi dengan benar.

4. **Business dashboard Metabase** berhasil dibuat dengan 15 visualisasi untuk monitoring status dan performa mahasiswa secara real-time.

5. **Prototype Streamlit** berhasil dibuat dan dapat digunakan tim akademik untuk prediksi risiko dropout mahasiswa secara individual.

### Rekomendasi Action Items

- **Pantau pembayaran UKT secara aktif** — segera lakukan outreach kepada mahasiswa yang terlambat membayar karena ini adalah prediktor dropout terkuat. Tawarkan opsi cicilan atau bantuan finansial.
- **Buat sistem early warning berbasis performa Semester 1** — mahasiswa dengan jumlah unit lulus < 3 di Semester 1 harus segera didampingi oleh konselor akademik sebelum memasuki Semester 2.
- **Perluas program beasiswa** — data menunjukkan pemegang beasiswa memiliki tingkat dropout lebih rendah. Perluasan program beasiswa dapat menjadi investasi jangka panjang untuk meningkatkan angka kelulusan.
- **Intervensi khusus untuk mahasiswa lebih tua** — mahasiswa yang mendaftar di usia > 25 tahun memiliki risiko dropout lebih tinggi, kemungkinan karena konflik antara studi dan tanggung jawab lainnya. Program kuliah malam atau fleksibel dapat membantu.
- **Gunakan prototype Streamlit sebagai alat kerja tim akademik** — staf dapat memasukkan data mahasiswa baru untuk mendapatkan prediksi risiko dropout secara real-time dan mengambil tindakan preventif lebih awal.
- **Evaluasi kurikulum program studi dengan dropout tinggi** — analisis dashboard per Course dapat mengidentifikasi program studi mana yang membutuhkan evaluasi kurikulum atau dukungan pengajaran tambahan.
