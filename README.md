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

Sumber data: ....

Setup environment:
```

```

## Business Dashboard
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

## 🌐 Link Akses Dashboard

🔗 [Klik di sini untuk membuka dashboard]([https://your-username-your-app.streamlit.app](https://student-performance-dashboard-qrk5mkxszrb5rrdfzchsob.streamlit.app/))

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
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
