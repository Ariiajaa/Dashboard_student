import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Student Dropout Predict — Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

# ── Load Model ───────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    clf = joblib.load("model_student.pkl")
    le  = joblib.load("label_encoder.pkl")
    return clf, le

clf, le = load_model()

# ── Header ───────────────────────────────────────────────────────────────────
st.title("🎓 Student Status Predict")
st.subheader("Jaya Jaya Institut — Student Perfome")
st.markdown(
    "Aplikasi ini memprediksi kemungkinan mahasiswa akan "
    "**Dropout**, **Graduate**, atau **Enrolled** "
    "berdasarkan data akademik dan demografis."
)
st.divider()

# ── Input Form ───────────────────────────────────────────────────────────────
st.header("📋 Input Data Mahasiswa")

col1, col2, col3 = st.columns(3)

# ── KOLOM 1: Demografis & Finansial ─────────────────────────────────────────
with col1:
    st.subheader("👤 Demografis")

    marital_status = st.selectbox(
        "Marital Status",
        options=[1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            1: "1 — Single",
            2: "2 — Married",
            3: "3 — Widower",
            4: "4 — Divorced",
            5: "5 — Facto Union",
            6: "6 — Separated"
        }[x]
    )

    gender = st.selectbox(
        "Gender",
        options=[0, 1],
        format_func=lambda x: "0 — Female" if x == 0 else "1 — Male"
    )

    # Usia: batas bawah 17 (usia minimum masuk kuliah)
    # batas atas 70 (sesuai data aktual)
    age_at_enrollment = st.slider(
        "Usia Saat Mendaftar (Age at Enrollment)",
        min_value=17,    # batas bawah: usia minimum mahasiswa
        max_value=70,    # batas atas: usia maksimum dalam data
        value=20,
        step=1,
        help="Rentang usia mahasiswa dalam data: 17 – 70 tahun"
    )

    international = st.selectbox(
        "Mahasiswa Internasional",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

    displaced = st.selectbox(
        "Displaced (Pindahan)",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

    educational_special = st.selectbox(
        "Kebutuhan Pendidikan Khusus",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

    st.subheader("💰 Finansial & Beasiswa")

    debtor = st.selectbox(
        "Memiliki Tunggakan (Debtor)",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

    tuition_up_to_date = st.selectbox(
        "UKT Dibayar Tepat Waktu",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

    scholarship_holder = st.selectbox(
        "Pemegang Beasiswa",
        options=[0, 1],
        format_func=lambda x: "0 — Tidak" if x == 0 else "1 — Ya"
    )

# ── KOLOM 2: Penerimaan & Kualifikasi ────────────────────────────────────────
with col2:
    st.subheader("📋 Penerimaan & Kualifikasi")

    application_mode = st.selectbox(
        "Application Mode",
        options=[1,2,5,7,10,15,16,17,18,26,27,39,42,43,44,51,53,57],
        index=5,
        help="Jalur pendaftaran mahasiswa"
    )

    application_order = st.slider(
        "Application Order (Prioritas Pilihan)",
        min_value=0,
        max_value=9,
        value=1,
        step=1,
        help="0 = pilihan pertama, 9 = pilihan terakhir"
    )

    course = st.selectbox(
        "Program Studi (Course)",
        options=[33, 171, 8014, 9003, 9070, 9085, 9119, 9130,
                 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991],
        format_func=lambda x: {
            33:   "33 — Biofuel Production Technologies",
            171:  "171 — Animation and Multimedia Design",
            8014: "8014 — Social Service (evening)",
            9003: "9003 — Agronomy",
            9070: "9070 — Communication Design",
            9085: "9085 — Veterinary Nursing",
            9119: "9119 — Informatics Engineering",
            9130: "9130 — Equinculture",
            9147: "9147 — Management",
            9238: "9238 — Social Service",
            9254: "9254 — Tourism",
            9500: "9500 — Nursing",
            9556: "9556 — Oral Hygiene",
            9670: "9670 — Advertising & Marketing Management",
            9773: "9773 — Journalism and Communication",
            9853: "9853 — Basic Education",
            9991: "9991 — Management (evening)",
        }[x],
        index=10
    )

    daytime_attendance = st.selectbox(
        "Waktu Kuliah",
        options=[0, 1],
        format_func=lambda x: "0 — Malam (Evening)" if x == 0 else "1 — Siang (Daytime)"
    )

    prev_qualification = st.selectbox(
        "Kualifikasi Sebelumnya",
        options=list(range(1, 18)),
        index=0,
        help="Jenis kualifikasi pendidikan sebelumnya"
    )

    prev_qual_grade = st.slider(
        "Nilai Kualifikasi Sebelumnya",
        min_value=95.0,
        max_value=190.0,
        value=133.0,
        step=0.5,
        help="Rentang dalam data: 95.0 – 190.0"
    )

    admission_grade = st.slider(
        "Nilai Masuk (Admission Grade)",
        min_value=95.0,
        max_value=190.0,
        value=126.0,
        step=0.5,
        help="Rentang dalam data: 95.0 – 190.0"
    )

    st.subheader("👨‍👩‍👧 Latar Belakang Keluarga")

    nacionality = st.slider(
        "Kode Nasionalitas",
        min_value=1,
        max_value=109,
        value=1,
        step=1
    )

    mothers_qual = st.slider(
        "Tingkat Pendidikan Ibu",
        min_value=1,
        max_value=44,
        value=19,
        step=1
    )

    fathers_qual = st.slider(
        "Tingkat Pendidikan Ayah",
        min_value=1,
        max_value=44,
        value=12,
        step=1
    )

    mothers_occ = st.slider(
        "Pekerjaan Ibu",
        min_value=0,
        max_value=194,
        value=5,
        step=1
    )

    fathers_occ = st.slider(
        "Pekerjaan Ayah",
        min_value=0,
        max_value=195,
        value=9,
        step=1
    )

# ── KOLOM 3: Akademik & Ekonomi ───────────────────────────────────────────────
with col3:
    st.subheader("📚 Performa Semester 1")

    cu1_credited = st.slider(
        "SKS Diakui Sem 1",
        min_value=0, max_value=20, value=0, step=1
    )
    cu1_enrolled = st.slider(
        "SKS Diambil Sem 1",
        min_value=0, max_value=26, value=6, step=1
    )
    cu1_evaluations = st.slider(
        "Jumlah Evaluasi Sem 1",
        min_value=0, max_value=45, value=8, step=1
    )
    cu1_approved = st.slider(
        "SKS Lulus Sem 1",
        min_value=0, max_value=26, value=5, step=1
    )
    cu1_grade = st.slider(
        "Nilai Rata-rata Sem 1",
        min_value=0.0, max_value=18.9, value=12.3, step=0.1,
        help="Rentang dalam data: 0.0 – 18.9"
    )
    cu1_no_eval = st.slider(
        "SKS Tanpa Evaluasi Sem 1",
        min_value=0, max_value=12, value=0, step=1
    )

    st.subheader("📚 Performa Semester 2")

    cu2_credited = st.slider(
        "SKS Diakui Sem 2",
        min_value=0, max_value=19, value=0, step=1
    )
    cu2_enrolled = st.slider(
        "SKS Diambil Sem 2",
        min_value=0, max_value=23, value=6, step=1
    )
    cu2_evaluations = st.slider(
        "Jumlah Evaluasi Sem 2",
        min_value=0, max_value=33, value=8, step=1
    )
    cu2_approved = st.slider(
        "SKS Lulus Sem 2",
        min_value=0, max_value=20, value=5, step=1
    )
    cu2_grade = st.slider(
        "Nilai Rata-rata Sem 2",
        min_value=0.0, max_value=18.6, value=12.2, step=0.1,
        help="Rentang dalam data: 0.0 – 18.6"
    )
    cu2_no_eval = st.slider(
        "SKS Tanpa Evaluasi Sem 2",
        min_value=0, max_value=12, value=0, step=1
    )

    st.subheader("🌍 Kondisi Makroekonomi")

    unemployment_rate = st.slider(
        "Tingkat Pengangguran (%)",
        min_value=7.6, max_value=16.2, value=11.1, step=0.1,
        help="Rentang dalam data: 7.6% – 16.2%"
    )
    inflation_rate = st.slider(
        "Tingkat Inflasi (%)",
        min_value=-0.8, max_value=3.7, value=1.4, step=0.1,
        help="Rentang dalam data: -0.8% – 3.7%"
    )
    gdp = st.slider(
        "GDP",
        min_value=-4.06, max_value=3.51, value=0.32, step=0.01,
        help="Rentang dalam data: -4.06 – 3.51"
    )

# ── Assemble Input ────────────────────────────────────────────────────────────
input_data = pd.DataFrame([{
    "Marital_status": marital_status,
    "Application_mode": application_mode,
    "Application_order": application_order,
    "Course": course,
    "Daytime_evening_attendance": daytime_attendance,
    "Previous_qualification": prev_qualification,
    "Previous_qualification_grade": prev_qual_grade,
    "Nacionality": nacionality,
    "Mothers_qualification": mothers_qual,
    "Fathers_qualification": fathers_qual,
    "Mothers_occupation": mothers_occ,
    "Fathers_occupation": fathers_occ,
    "Admission_grade": admission_grade,
    "Displaced": displaced,
    "Educational_special_needs": educational_special,
    "Debtor": debtor,
    "Tuition_fees_up_to_date": tuition_up_to_date,
    "Gender": gender,
    "Scholarship_holder": scholarship_holder,
    "Age_at_enrollment": age_at_enrollment,
    "International": international,
    "Curricular_units_1st_sem_credited": cu1_credited,
    "Curricular_units_1st_sem_enrolled": cu1_enrolled,
    "Curricular_units_1st_sem_evaluations": cu1_evaluations,
    "Curricular_units_1st_sem_approved": cu1_approved,
    "Curricular_units_1st_sem_grade": cu1_grade,
    "Curricular_units_1st_sem_without_evaluations": cu1_no_eval,
    "Curricular_units_2nd_sem_credited": cu2_credited,
    "Curricular_units_2nd_sem_enrolled": cu2_enrolled,
    "Curricular_units_2nd_sem_evaluations": cu2_evaluations,
    "Curricular_units_2nd_sem_approved": cu2_approved,
    "Curricular_units_2nd_sem_grade": cu2_grade,
    "Curricular_units_2nd_sem_without_evaluations": cu2_no_eval,
    "Unemployment_rate": unemployment_rate,
    "Inflation_rate": inflation_rate,
    "GDP": gdp,
}])

# ── Predict Button ────────────────────────────────────────────────────────────
st.divider()
predict_btn = st.button(
    "🔮 Prediksi Status Mahasiswa",
    use_container_width=True,
    type="primary"
)

if predict_btn:
    pred_enc   = clf.predict(input_data)[0]
    pred_label = le.inverse_transform([pred_enc])[0]
    pred_proba = clf.predict_proba(input_data)[0]
    proba_dict = dict(zip(le.classes_, pred_proba))

    st.header("🔮 Hasil Prediksi")

    emoji_map = {"Dropout": "🔴", "Enrolled": "🟡", "Graduate": "🟢"}
    emoji = emoji_map.get(pred_label, "⚪")

    # KPI metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Status Prediksi", f"{emoji} {pred_label}")
    m2.metric("Probabilitas Dropout",  f"{proba_dict.get('Dropout', 0)*100:.1f}%")
    m3.metric("Probabilitas Enrolled", f"{proba_dict.get('Enrolled', 0)*100:.1f}%")
    m4.metric("Probabilitas Graduate", f"{proba_dict.get('Graduate', 0)*100:.1f}%")

    st.divider()

    res1, res2 = st.columns([1, 1])

    with res1:
        st.subheader("📊 Probabilitas per Kelas")
        for label, prob in sorted(proba_dict.items(), key=lambda x: -x[1]):
            st.markdown(f"**{label}**")
            st.progress(float(prob), text=f"{prob*100:.1f}%")

    with res2:
        st.subheader("💡 Interpretasi & Rekomendasi")
        if pred_label == "Dropout":
            st.error(
                "⚠️ **RISIKO TINGGI — Diprediksi DROPOUT**\n\n"
                "**Tindakan yang disarankan:**\n"
                "- Segera hubungi mahasiswa untuk sesi konseling akademik\n"
                "- Cek status pembayaran UKT dan tawarkan bantuan finansial\n"
                "- Evaluasi beban SKS dan sesuaikan kemampuan mahasiswa\n"
                "- Berikan program pendampingan belajar intensif\n"
                "- Libatkan orang tua/wali jika diperlukan"
            )
        elif pred_label == "Enrolled":
            st.warning(
                "📘 **PERLU DIPANTAU — Masih ENROLLED**\n\n"
                "**Tindakan yang disarankan:**\n"
                "- Pantau perkembangan akademik secara berkala\n"
                "- Berikan motivasi dan dukungan belajar tambahan\n"
                "- Pastikan tidak ada kendala finansial atau personal\n"
                "- Dorong partisipasi aktif dalam kegiatan akademik"
            )
        else:
            st.success(
                "✅ **PROGRES BAIK — Diprediksi GRADUATE**\n\n"
                "**Tindakan yang disarankan:**\n"
                "- Pertahankan dukungan akademik yang sudah berjalan\n"
                "- Dorong partisipasi dalam kegiatan kemahasiswaan\n"
                "- Siapkan program career development & magang\n"
                "- Jadikan sebagai role model bagi mahasiswa lain"
            )

    st.divider()
    st.subheader("📋 Ringkasan Data Input")
    st.dataframe(
        input_data.T.rename(columns={0: "Nilai Input"}),
        use_container_width=True
    )

st.divider()
st.markdown(
    "**⚠️ Catatan**: Prediksi ini bersifat indikatif dan merupakan alat bantu keputusan. "
    "Keputusan akhir tetap berada di tangan tim akademik."
)
st.caption(
    "Jaya Jaya Institut | Student Early Warning System | "
    "Powered by Random Forest Classifier | "
    "Data: 4.424 mahasiswa"
)