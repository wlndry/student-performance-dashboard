# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
**Jaya Jaya Institut** merupakan sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama dua dekade, institusi ini dikenal telah meluluskan banyak alumni berkualitas. Namun, dalam beberapa tahun terakhir, mereka menghadapi permasalahan serius, yaitu **tingginya angka dropout (putus kuliah) dari para siswa**.

Fenomena ini tentu mengganggu reputasi dan performa institusi. Jika tidak ditangani secara serius, dropout dapat berdampak pada akreditasi, kepercayaan masyarakat, hingga keberlanjutan institusi. Untuk itu, **Jaya Jaya Institut** ingin memanfaatkan data historis performa siswa guna **memprediksi kemungkinan dropout secara dini**, agar pihak kampus dapat memberikan intervensi atau bimbingan lebih awal kepada siswa yang berisiko tinggi.

---

### Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang ingin diselesaikan dalam proyek ini:

1. **Tingginya angka dropout mahasiswa** di Jaya Jaya Institut yang berdampak negatif pada reputasi dan performa institusi.
2. **Tidak adanya sistem deteksi dini** untuk mengetahui siswa yang berisiko dropout, sehingga institusi terlambat dalam melakukan intervensi.
3. **Minimnya pemanfaatan data historis siswa** untuk mendukung pengambilan keputusan yang berbasis data (data-driven decision making).
4. **Kebutuhan akan sistem yang mampu memvisualisasikan dan memonitor kondisi siswa** secara mudah dan interaktif melalui dashboard.

---

### Cakupan Proyek
Untuk menjawab tantangan dari Jaya Jaya Institut, kita akan melakukan hal-hal berikut:

- Mengembangkan **model machine learning** untuk memprediksi kemungkinan siswa melakukan dropout berdasarkan data historis.
- Melakukan **eksplorasi data (EDA)** untuk memahami pola dan insight dari performa siswa.
- Membuat **dashboard interaktif menggunakan Metabase** untuk memvisualisasikan performa siswa.
- Membuat **prototipe aplikasi** berbasis Streamlit yang memungkinkan user menginput data siswa dan mendapatkan prediksi risiko dropout secara langsung.
- Memberikan **rekomendasi action items** berdasarkan hasil analisis data.

### Persiapan

### Sumber Data  
Dataset yang digunakan dalam proyek ini berjudul **Students' Performance** dan diperoleh dari repositori GitHub.

🔗 [Students' Performance – GitHub Repository](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

### Setup Environment  
Ikuti langkah-langkah berikut untuk menyiapkan dan menjalankan proyek ini di lingkungan lokal Anda:

#### 1. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv venv
```
#### 2. Aktifkan Virtual Environment
Windows:
```bash
.\venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
#### 3. Install Dependensi
Instal semua dependensi yang dibutuhkan dari file requirements.txt:
```bash
pip install -r requirements.txt
```
#### 4. Jalankan Notebook Analisis
Silakan buka file **`notebook.ipynb`** menggunakan **Jupyter Notebook** atau **ekstensi Jupyter di VSCode**, lalu jalankan semua sel satu per satu untuk melakukan proses eksplorasi dan analisis terhadap data yang tersedia.

#### 5. Jalankan Dashboard Visualisasi
Untuk menjalankan dashboard berbasis Streamlit secara lokal, gunakan perintah berikut:

```bash
streamlit run dashboard.py
```
Tunggu hingga browser otomatis terbuka. Jika tidak, buka secara manual alamat yang diberikan, biasanya:

```
http://localhost:8501
```

#### 6. Jalankan Prototype Prediksi
Untuk menjalankan prototype Streamlit secara lokal, gunakan perintah berikut:

```bash
streamlit run app.py
```
Tunggu hingga browser otomatis terbuka. Jika tidak, buka secara manual alamat yang diberikan, biasanya:

```
http://localhost:8501
```

## Business Dashboard
![dashboard](https://github.com/user-attachments/assets/79f4520e-4dd1-4b17-9d0e-438d194351a3)

### 🧾 Deskripsi Umum

Dashboard ini dirancang untuk memvisualisasikan performa mahasiswa berdasarkan data yang dikumpulkan dari institusi pendidikan tinggi. Tujuan dari dashboard ini adalah untuk memberikan **insight analitis** terhadap karakteristik demografis, sosial-ekonomi, dan akademik mahasiswa, serta performa mereka selama dua semester pertama kuliah.
Dashboard berfokus pada **eksplorasi data** secara visual untuk mendukung pengambilan keputusan oleh stakeholder akademik, seperti dosen, manajer program studi, dan pihak administrasi kampus.

---

### 🔍 Fitur Utama

#### 1. Overview
Menampilkan gambaran umum dataset dan penjelasan fitur-fitur penting, termasuk tujuan analisis dan struktur data.

#### 2. Distribusi Target
Visualisasi distribusi status akhir mahasiswa (Dropout, Graduate, Enrolled) untuk melihat komposisi keseluruhan outcome.

#### 3. Data Demografis
Analisis terhadap:
- Jenis kelamin (`Gender`)
- Usia saat pendaftaran (`Age at enrollment`)
- Status pernikahan (`Marital status`)
- Asal daerah (`Displaced`)
- Kebangsaan (`Nationality`)
- Status internasional

#### 4. Data Sosial-Ekonomi
Analisis pekerjaan dan pendidikan orang tua, status beasiswa, status pembayaran, kebutuhan khusus, serta indikator ekonomi (tingkat pengangguran, inflasi, GDP).

#### 5. Data Akademik Sebelum Kuliah
Meliputi mode pendaftaran, urutan pilihan, nilai masuk (`Admission grade`), dan kualifikasi sebelumnya.

#### 6. Performa Akademik Semester 1 & 2
Visualisasi performa mahasiswa berdasarkan:
- Mata kuliah yang diambil, lulus, dan dinilai
- Nilai rata-rata
- Jumlah mata kuliah tanpa evaluasi

---

### 🛠️ Teknologi yang Digunakan

- **Python**
- **Streamlit**: Antarmuka dashboard interaktif
- **Pandas**: Pengolahan data
- **Seaborn & Matplotlib**: Visualisasi grafik
---

### 🌐 Link Akses Dashboard

🔗 [Klik di sini untuk membuka dashboard](https://student-performance-dashboard-qrk5mkxszrb5rrdfzchsob.streamlit.app/)

---

### 📂 Struktur Menu Dashboard

| Menu                        | Konten Visualisasi                              |
|----------------------------|--------------------------------------------------|
| Overview                   | Deskripsi dataset & penjelasan kolom            |
| Distribusi Target          | Countplot status mahasiswa                      |
| Data Demografis            | Boxplot / Countplot data demografi              |
| Data Sosial-Ekonomi        | Visualisasi kondisi sosial & ekonomi            |
| Data Akademik Sebelum Kuliah| Nilai & riwayat akademik saat pendaftaran      |
| Performa Semester 1        | Nilai & evaluasi mata kuliah semester 1         |
| Performa Semester 2        | Nilai & evaluasi mata kuliah semester 2         |

---


## Menjalankan Sistem Machine Learning
![localhost_8501_ (1)](https://github.com/user-attachments/assets/8445c82e-7225-44bd-98c6-09f767182c71)

Prototype ini merupakan aplikasi web interaktif berbasis **Streamlit** yang digunakan untuk memprediksi **status mahasiswa**:  
- 🔴 Dropout  
- 🟢 Enrolled  
- 🎓 Graduate  

Prediksi dilakukan berdasarkan data sosiodemografis, nilai akademik semester awal, serta beberapa indikator ekonomi. Aplikasi ini menggunakan model **Random Forest Classifier** yang telah dilatih dan disimpan dalam file `model.pkl`.

### 📥 Input Pengguna

Pengguna akan diminta mengisi data melalui form antarmuka web dengan dua kolom. Input mencakup:

#### 🔹 Data Sosial dan Demografis:
- **Marital Status** (Single, Married, dll.)
- **Application Mode** (1st phase, Transfer, dll.)
- **Gender**
- **Age at Enrollment**
- **Nationality**
- **Displaced**
- **Special Needs**
- **Debtor**
- **Tuition Fees Up To Date**
- **Scholarship Holder**
- **International**

#### 🔹 Data Akademik:
- **Application Order**
- **Course**
- **Previous Qualification** & **Grade**
- **Admission Grade**
- **Mother's/Father's Qualification** & **Occupation**
- **Data Semester 1 & 2:**
  - **Credited**
  - **Enrolled**
  - **Evaluated**
  - **Approved**
  - **Grade**
  - **Without Evaluation**

#### 🔹 Data Ekonomi:
- **Unemployment Rate (%)**
- **Inflation Rate (%)**
- **GDP (x1000)**

---

### ✅ Output Aplikasi

Setelah pengguna menekan tombol **"🔍 Prediksi Status"**, sistem akan memproses input dan menampilkan prediksi status mahasiswa.

Contoh hasil prediksi:

- 🔴 **Dropout**
- 🟢 **Enrolled**
- 🎓 **Graduate**

### 🌐 Link Akses Prototype

🔗 [Klik di sini untuk membuka prototype](https://student-performance-prediction-f6eybl9m9wvjlfmmhvylgx.streamlit.app/)

### 🔧 Langkah-Langkah Menjalankan Prototipe Sistem Machine Learning

#### 1. Aktifkan Virtual Environment (Opsional, tetapi direkomendasikan)

```bash
# Untuk Windows
python -m venv venv
venv\Scripts\activate

# Untuk MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install Dependensi
Pastikan Anda sudah berada di dalam direktori proyek, lalu jalankan:

```bash
pip install -r requirements.txt
```

#### 3. Siapkan Model
Pastikan file `model.pkl` (hasil training model machine learning) sudah ada di dalam direktori yang sama dengan `app.py`.

Jika belum, jalankan notebook.ipynb untuk menghasilkan file `model.pkl`.

---

#### 4. Jalankan Aplikasi Streamlit

Untuk menjalankan aplikasi prediksi status mahasiswa berbasis Streamlit, gunakan perintah berikut:

```bash
streamlit run app.py
```

Tunggu hingga browser otomatis terbuka. Jika tidak, buka secara manual alamat yang diberikan, biasanya:

```
http://localhost:8501
```

---

#### 5. Masukkan Data Input
Setelah aplikasi berjalan, pengguna diminta untuk mengisi formulir prediksi yang terbagi menjadi beberapa bagian:

- **Data Sosial dan Demografis**
- **Data Akademik**
- **Data Ekonomi**

Isi sesuai kondisi mahasiswa yang ingin diprediksi.

---

#### 6. Lihat Hasil Prediksi
Klik tombol **🔍 Prediksi Status**, dan sistem akan menampilkan status mahasiswa berdasarkan model yang telah dilatih, seperti:

- 🔴 Dropout
- 🟢 Enrolled
- 🎓 Graduate

---

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
