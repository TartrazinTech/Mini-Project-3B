# Analisis Efisiensi Pengeluaran dan Klasifikasi Tingkat Profitabilitas pada Perusahaan Startup

## 1. Deskripsi Project
Mini Project ini merupakan program pengolahan dan analisis data menggunakan bahasa pemrograman Python untuk menganalisis efisiensi pengeluaran dan mengklasifikasikan tingkat profitabilitas perusahaan startup.
Program menggunakan dataset `50_Startups.csv` yang terdiri dari 50 perusahaan startup di tiga wilayah, yaitu New York, California, dan Florida. Data yang dianalisis meliputi Research and Development (R&D) Spend, Administration, Marketing Spend, State, dan Profit.
Pengolahan dilakukan untuk mengetahui total pengeluaran, rasio efisiensi, kategori profitabilitas, serta perbandingan kinerja startup berdasarkan wilayah. Program juga dilengkapi dengan sistem validasi data, pengurutan ranking, rekapitulasi, dan menu interaktif untuk mempermudah pengguna dalam mengakses hasil analisis.

## 2. Tujuan Program
1. Mengolah dataset startup menggunakan bahasa pemrograman Python.
2. Memvalidasi kelengkapan dan keabsahan data sebelum dilakukan analisis.
3. Menghitung total pengeluaran setiap startup.
4. Menghitung rasio efisiensi berdasarkan perbandingan profit dan total pengeluaran.
5. Mengklasifikasikan tingkat efisiensi startup berdasarkan kriteria yang ditentukan.
6. Menghasilkan rekapitulasi rata-rata kinerja startup berdasarkan State.
7. Menyusun ranking startup berdasarkan efisiensi tertinggi hingga terendah.
8. Memberikan informasi dan saran perbaikan berdasarkan hasil analisis.
9. Menyajikan hasil pengolahan data melalui menu interaktif.

## 3. Dataset
Dataset yang digunakan adalah `50_Startups.csv` yang memuat 50 data startup dengan lima kolom utama.
| Kolom | Keterangan |
|---|---|
| R&D Spend | Pengeluaran penelitian dan pengembangan |
| Administration | Pengeluaran administrasi |
| Marketing Spend | Pengeluaran pemasaran |
| State | Wilayah startup |
| Profit | Keuntungan yang diperoleh |

## 4. Fitur Program
### A. Tampilan Identitas Program
1. Menampilkan cover Mini Project secara langsung pada terminal ketika program dijalankan.
2. Menampilkan judul proyek, identitas kelompok, anggota, asisten pembimbing, dan dosen pengampu.

### B. Identifikasi Pengguna
1. Meminta identitas pengguna sebelum mengakses menu program.
2. Melakukan verifikasi password.
3. Membatasi percobaan ketika pengguna memasukkan password yang salah.
4. Menampilkan sapaan berdasarkan nama dan peran pengguna.
5. Menyediakan pilihan untuk mengakhiri sesi pengguna.

### C. Pengolahan dan Validasi Data
1. Membaca dataset berformat CSV.
2. Memeriksa keberadaan file dataset.
3. Memvalidasi kelengkapan header dan kolom wajib.
4. Mendeteksi data kosong dan nilai non-angka.
5. Mendeteksi nilai negatif pada variabel numerik.
6. Mendeteksi total pengeluaran yang bernilai nol.
7. Memisahkan data valid dan tidak valid.
8. Menampilkan data tidak valid beserta alasan kesalahannya.

### D. Analisis Efisiensi
1. Menghitung total pengeluaran setiap startup.
2. Menghitung rasio efisiensi berdasarkan Profit dan total pengeluaran.
3. Mengklasifikasikan tingkat efisiensi menjadi kategori Tinggi, Sedang, dan Rendah.
4. Mengurutkan startup berdasarkan efisiensi.
5. Memberikan nomor peringkat pada setiap startup.

### E. Rekapitulasi dan Hasil Analisis
1. Menghitung rata-rata pengeluaran dan profit berdasarkan State.
2. Menghitung rata-rata efisiensi setiap State.
3. Menghitung jumlah startup berdasarkan kategori efisiensi.
4. Menampilkan ringkasan hasil pengolahan data.
5. Menampilkan kesimpulan berdasarkan hasil analisis.

### F. Menu Interaktif
Program menyediakan lima pilihan menu utama.
1. Ranking Keseluruhan: Menampilkan ranking efisiensi seluruh startup, ringkasan data, dan kesimpulan hasil analisis.
2. Top N / Bottom N: Menampilkan sejumlah startup dengan efisiensi tertinggi atau terendah berdasarkan jumlah yang dimasukkan pengguna.
3. Rekapitulasi per State: Menampilkan hasil rekapitulasi dan ranking startup berdasarkan wilayah.
4. Saran dan Solusi: Menampilkan saran perbaikan berdasarkan perbandingan komposisi pengeluaran dan hasil profitabilitas startup.
5. Keluar: Mengakhiri sesi pengguna dan kembali ke proses identifikasi pengguna.

## 5. Rumus Perhitungan

Total Pengeluaran = R&D Spend + Administration + Marketing Spend
Rasio Efisiensi = Profit / Total Pengeluaran
Nilai rasio efisiensi digunakan sebagai dasar pengelompokan kategori dan pengurutan ranking startup.

## 6. Kriteria Klasifikasi
| Kategori | Nilai Efisiensi |
|---|---|
| Tinggi | Lebih besar dari atau sama dengan 0,30 |
| Sedang | Lebih besar dari atau sama dengan 0,26 dan kurang dari 0,30 |
| Rendah | Kurang dari 0,26 |

Klasifikasi dilakukan berdasarkan nilai rasio efisiensi yang diperoleh dari perbandingan profit terhadap total pengeluaran setiap startup.

## 7. Cara Menjalankan Program
1. Unduh atau clone repository GitHub.
2. Pastikan Python telah terpasang pada komputer.
3. Simpan file `50_Startups.csv` dan `mp coding.py` dalam folder yang sama.
4. Buka terminal atau command prompt pada folder project.
5. Jalankan perintah berikut:
   ```bash
   python "mp coding.py"
   ```
6. Program akan menampilkan cover Mini Project pada terminal.
7. Lakukan identifikasi pengguna dan verifikasi password.
8. Setelah berhasil, pengguna dapat mengakses menu utama.
9. Pilih menu yang tersedia untuk melihat hasil analisis sesuai kebutuhan.

## 8. Struktur Repository
```text
Mini-Project-3B/
│
├── 50_Startups.csv
├── MP 3B mk1.docx
├── Proposal Pengajuan Judul Mini Project.docx
├── mp coding.py
└── README.md
```

## 9. Output Program
Program menghasilkan beberapa keluaran utama:
1. Tampilan cover dan identitas Mini Project pada terminal.
2. Informasi identifikasi pengguna dan verifikasi akses.
3. Ranking efisiensi seluruh startup dari tertinggi hingga terendah.
4. Hasil pemilihan Top N dan Bottom N.
5. Rekapitulasi rata-rata pengeluaran, profit, dan efisiensi berdasarkan State.
6. Ringkasan jumlah startup berdasarkan kategori efisiensi.
7. Kesimpulan startup dengan efisiensi tertinggi dan terendah.
8. Daftar data tidak valid beserta alasan kesalahannya.
9. Informasi dan saran perbaikan berdasarkan hasil analisis startup.

## 10. Batasan Project
1. Analisis hanya menggunakan dataset yang terdiri dari 50 startup.
2. Program menggunakan dataset CSV sebagai sumber data utama dan tidak menerima input transaksi secara langsung.
3. Analisis terbatas pada lima variabel yang tersedia dalam dataset.
4. Perhitungan efisiensi menggunakan perbandingan Profit terhadap total pengeluaran.
5. Klasifikasi efisiensi menggunakan batas kategori yang telah ditentukan.
6. Program tidak digunakan untuk memprediksi profit masa depan.
7. Saran perbaikan yang diberikan merupakan hasil analisis data dan bukan keputusan bisnis yang mutlak.
UNIVERSITAS ANDALAS

2026
