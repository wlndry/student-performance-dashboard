import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import missingno as msno

# Pengaturan tampilan
st.set_page_config(page_title="Student Perfomace Dashboard", layout="wide")
st.title("🎓 Student Perfomace Dashboard")

# Load dataset
url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv"
df = pd.read_csv(url, delimiter=';')





# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Analisis",
    (
        "Overview",
        "Distribusi Target",
        "Data Demografis",
        "Data Sosial-Ekonomi",
        "Data Akademik Sebelum Kuliah",
        "Performa Semester 1",
        "Performa Semester 2"
    )
)

# Gambaran umum dan penjelasan kolom
if menu == "Overview":
    description = """
    ## 📘 Gambaran Umum Dataset

    Dashboard ini menampilkan analisis data dan prediksi performa mahasiswa berdasarkan data yang diperoleh dari sebuah institusi pendidikan tinggi. Dataset mencakup informasi dari mahasiswa berbagai program studi sarjana, seperti **Agronomi, Desain, Pendidikan, Keperawatan, Jurnalistik, Manajemen, Pelayanan Sosial**, dan **Teknologi**.

    Dataset ini berisi informasi yang diketahui saat mahasiswa **pertama kali mendaftar**, termasuk:

    - **Karakteristik demografis & sosial ekonomi** (usia, jenis kelamin, status pernikahan, kebangsaan, pekerjaan & pendidikan orang tua)
    - **Latar belakang akademik** (kualifikasi sebelumnya, nilai masuk, status beasiswa)
    - **Performa akademik semester 1 dan 2** (jumlah mata kuliah yang diambil, dinilai, lulus)
    - **Status akhir** mahasiswa: apakah **dropout**, **aktif**, atau **lulus**

    Tujuan utama dari analisis ini adalah untuk:
    - Mengidentifikasi faktor-faktor utama yang memengaruhi keberhasilan atau kegagalan mahasiswa
    - Membangun model prediktif untuk memperkirakan kemungkinan **drop out**
    - Membantu lembaga pendidikan dalam mengambil **keputusan intervensi dini** demi meningkatkan **retensi mahasiswa**
    """
    st.markdown(description)

    with st.expander("🔎 Penjelasan Kolom Dataset"):
        st.markdown("""
        **Contoh beberapa kolom penting dalam dataset:**

        - `Status`: Status akhir mahasiswa (Dropout, Graduate, Enrolled)
        - `Gender`: Jenis kelamin mahasiswa (1 – laki-laki, 0 – perempuan)
        - `Age at enrollment`: Usia mahasiswa saat pendaftaran
        - `Scholarship holder`: Status beasiswa (1 – penerima, 0 – bukan)
        - `Admission grade`: Nilai ujian masuk (rentang 0–200)
        - `Displaced`: Apakah mahasiswa berasal dari luar daerah (1 – ya, 0 – tidak)
        - `Educational special needs`: Memiliki kebutuhan khusus (1 – ya, 0 – tidak)
        - `Curricular units 1st sem (credited)`: Jumlah mata kuliah yang diakui (transfer kredit) di semester 1
        - `Curricular units 1st sem (enrolled)`: Jumlah mata kuliah yang diambil semester 1
        - `Curricular units 1st sem (evaluations)`: Jumlah mata kuliah yang dinilai semester 1
        - `Curricular units 1st sem (approved)`: Jumlah mata kuliah yang lulus semester 1

        #### 🏷️ Kolom Kategorikal dan Makna Angkanya:

        - `Marital status`:
            - 1: Lajang, 2: Menikah, 3: Duda/Janda, 4: Cerai, 5: Hidup bersama, 6: Pisah hukum

        - `Application mode`:
            - 1: Jalur umum fase 1, 5: Jalur khusus Azores, 15: Mahasiswa internasional, 17: Jalur umum fase 2, 39: Usia > 23 tahun, 42: Pindahan, dll.

        - `Previous qualification`:
            - 1: SMA, 3: S1, 4: S2, 9-19: Menengah bawah atau tidak selesai

        - `Nationality`:
            - 1: Portugal, 2: Jerman, 6: Spanyol, 14: Inggris, 21: Angola, 41: Brasil, 103: Ukraina, dll.

        - `Mother's/Father's qualification`:
            - 1: SMA, 2–5: Perguruan tinggi, 34: Tidak diketahui, 35–37: Tidak bisa baca/tulis–SD

        - `Mother's/Father's occupation`:
            - 0: Mahasiswa, 1: Eksekutif, 2: Profesional, 4: Admin, 5: Jasa, 9: Pekerja kasar, 99: Kosong

        - `Tuition fees up to date`, `Debtor`, `Educational special needs`, `Displaced`, `Scholarship holder`, `International`:
            - 1: Ya, 0: Tidak
        """)

# 3. Distribusi Target
elif menu == "Distribusi Target":
    st.subheader("🎯 Distribusi Status Mahasiswa")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="Status", palette="Set2", ax=ax)
    st.pyplot(fig)

    # 3. Distribusi Target
elif menu == "Distribusi Target":
    st.subheader("🎯 Distribusi Status Mahasiswa")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="Status", palette="Set2", ax=ax)
    st.pyplot(fig)

# 4. Data Demografis
elif menu == "Data Demografis":
    st.subheader("🧍‍♂️ Data Demografis Mahasiswa")
    demographic_cols = [
        "Marital_status", "Gender", "Age_at_enrollment", 
        "Nacionality", "International", "Displaced"
    ]
    for col in demographic_cols:
        st.markdown(f"**{col}**")
        fig, ax = plt.subplots()
        if df[col].nunique() <= 10:
            sns.countplot(data=df, x=col, hue="Status", palette="Set1", ax=ax)
        else:
            sns.boxplot(data=df, x="Status", y=col, palette="Set1", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 5. Data Sosial-Ekonomi
elif menu == "Data Sosial-Ekonomi":
    st.subheader("💰 Data Sosial-Ekonomi Mahasiswa")
    socio_cols = [
        "Mothers_qualification", "Fathers_qualification",
        "Mothers_occupation", "Fathers_occupation",
        "Scholarship_holder", "Debtor", "Tuition_fees_up_to_date",
        "Educational_special_needs", "Unemployment_rate", 
        "Inflation_rate", "GDP"
    ]
    for col in socio_cols:
        st.markdown(f"**{col}**")
        fig, ax = plt.subplots()
        if df[col].nunique() <= 10:
            sns.countplot(data=df, x=col, hue="Status", palette="Set2", ax=ax)
        else:
            sns.boxplot(data=df, x="Status", y=col, palette="Set2", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 6. Data Akademik Sebelum Kuliah
elif menu == "Data Akademik Sebelum Kuliah":
    st.subheader("📚 Data Akademik Sebelum Kuliah")
    academic_pre_cols = [
        "Previous_qualification", "Previous_qualification_grade",
        "Application_mode", "Application_order", "Course", 
        "Admission_grade", "Daytime_evening_attendance"
    ]
    for col in academic_pre_cols:
        st.markdown(f"**{col}**")
        fig, ax = plt.subplots()
        if df[col].nunique() <= 10:
            sns.countplot(data=df, x=col, hue="Status", palette="Set3", ax=ax)
        else:
            sns.boxplot(data=df, x="Status", y=col, palette="Set3", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 7. Performa Semester 1
elif menu == "Performa Semester 1":
    st.subheader("📈 Performa Akademik Semester 1")
    sem1_cols = [
        "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_evaluations", "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade", "Curricular_units_1st_sem_without_evaluations"
    ]
    for col in sem1_cols:
        st.markdown(f"**{col}**")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Status", y=col, palette="coolwarm", ax=ax)
        st.pyplot(fig)

# 8. Performa Semester 2
elif menu == "Performa Semester 2":
    st.subheader("📊 Performa Akademik Semester 2")
    sem2_cols = [
        "Curricular_units_2nd_sem_credited", "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_evaluations", "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade", "Curricular_units_2nd_sem_without_evaluations"
    ]
    for col in sem2_cols:
        st.markdown(f"**{col}**")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Status", y=col, palette="viridis", ax=ax)
        st.pyplot(fig)
