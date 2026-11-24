Analisis Efisiensi Pengeluaran dan Klasifikasi Tingkat Profitabilitas pada Perusahaan Startup

1. Deskripsi Project
Mini Project ini merupakan program pengolahan data menggunakan bahasa pemrograman Python untuk menganalisis efisiensi pengeluaran dan mengklasifikasikan tingkat profitabilitas perusahaan startup.
Program menggunakan dataset yang terdiri dari 50 startup di tiga wilayah, yaitu New York, California, dan Florida. Data yang dianalisis meliputi Research and Development (R&D) Spend, Administration, Marketing Spend, State, dan Profit.
Pengolahan dilakukan untuk mengetahui total pengeluaran, rasio efisiensi, kategori profitabilitas, serta perbandingan kinerja startup berdasarkan wilayah.

2. Tujuan Program
    1. Menghitung total pengeluaran setiap startup.
    2. Menghitung rasio efisiensi berdasarkan perbandingan profit dan total pengeluaran.
    3. Mengklasifikasikan tingkat profitabilitas startup.
    4. Menghasilkan rekapitulasi rata-rata kinerja berdasarkan State.
    5. Menyusun ranking startup berdasarkan efisiensi tertinggi hingga terendah.

3. Dataset
Dataset yang digunakan adalah `50_Startups.csv` yang memuat 50 data startup dengan lima kolom utama:
|       Kolom      |                Keterangan               |
|------------------|-----------------------------------------|
| R&D Spend        | Pengeluaran penelitian dan pengembangan |
| Administration   | Pengeluaran administrasi                |
| Marketing Spend  | Pengeluaran pemasaran                   |
| State            | Wilayah startup                         |
| Profit           | Keuntungan yang diperoleh               |

4. Fitur Program
    1. Membaca dataset berformat CSV.
    2. Memvalidasi kelengkapan kolom dan nilai data.
    3. Mendeteksi data kosong, non-angka, nilai negatif, dan total pengeluaran nol.
    4. Menghitung total pengeluaran setiap startup.
    5. Menghitung rasio efisiensi.
    6. Mengklasifikasikan profitabilitas.
    7. Menghitung rekapitulasi rata-rata berdasarkan State.
    8. Mengurutkan ranking efisiensi startup.
    9. Menampilkan ringkasan dan kesimpulan hasil analisis.
    10. Menampilkan data yang tidak valid beserta alasannya.

5. Rumus Perhitungan
Total Pengeluaran = R&D Spend + Administration + Marketing Spend
Rasio Efisiensi = Profit / Total Pengeluaran

6. Kriteria Klasifikasi
| Kategori |                   Nilai Efisiensi                         |
|----------|-------------------------------------------------------------|
| Tinggi   | Lebih besar dari atau sama dengan 0,30                      |
| Sedang   | Lebih besar dari atau sama dengan 0,26 dan kurang dari 0,30 |
| Rendah   | Kurang dari 0,26                                            |

7. Cara Menjalankan Program
    1. Unduh atau clone repository GitHub.
    2. Pastikan Python telah terpasang.
    3. Simpan file `50_Startups.csv` dan `mp coding.py` dalam folder yang sama.
    4. Buka terminal atau command prompt.
    5. Jalankan perintah berikut:
        ```bash
        python "mp coding.py"
        ```
    6. Program akan membaca dataset, melakukan validasi, menghitung efisiensi, dan menampilkan hasil analisis.

8. Struktur Repository
    ```text
    Mini-Project-3B/
        50_Startups.csv
        MP 3B mk1.docx
        Proposal Pengajuan Judul Mini Project.docx
        mp coding.py
        README.md
    ```

9. Output Program
Program menghasilkan beberapa keluaran utama:
    1. Ranking efisiensi seluruh startup.
    2. Rekapitulasi rata-rata pengeluaran, profit, dan efisiensi berdasarkan State.
    3. Ringkasan jumlah startup berdasarkan kategori profitabilitas.
    4. Kesimpulan startup dengan efisiensi tertinggi dan terendah.
    5. Daftar data tidak valid beserta alasan kesalahannya.

10. Batasan Project
    1. Analisis hanya menggunakan dataset 50 startup.
    2. Program tidak menerima input transaksi secara langsung.
    3. Analisis terbatas pada lima variabel yang tersedia dalam dataset.
    4. Program tidak memprediksi profit masa depan.
    5. Hasil analisis merupakan informasi pendukung evaluasi, bukan keputusan mutlak.
