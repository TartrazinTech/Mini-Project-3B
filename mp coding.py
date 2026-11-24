import csv
import os
file_csv=r"50_Startups.csv"
Kolom_Wajib=["R&D Spend", "Administration", "Marketing Spend", "State", "Profit"]
Kolom_Teks=["State"]
Kolom_Angka=["R&D Spend", "Administration", "Marketing Spend", "Profit"]
BATAS_TINGGI = 0.30    
BATAS_SEDANG = 0.26
def buka_file(file_csv, kolom_wajib):
    if not os.path.exists(file_csv):
        return "File tidak ditemukan"
    with open (file_csv, "r") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            return "Dataset kosong atau tidak memiliki header."
        kolom_hilang = [kolom for kolom in kolom_wajib if kolom not in reader.fieldnames]
        if len(kolom_hilang) > 0:
            return "Kolom yang hilang: " + str(kolom_hilang)
    return ""
def validasi_baris(row, kolom_teks, kolom_angka):
    for kolom in kolom_teks:
        if row[kolom] is None or row[kolom].strip() == "":
            return "kolom " + kolom + " kosong."
    for kolom in kolom_angka:
        try:
            float(row[kolom])
        except (ValueError, TypeError):
                return "kolom " + kolom + " kosong atau bukan angka."
    for kolom in kolom_angka:
        if float(row[kolom]) < 0:
             return "kolom " + kolom + " bernilai negatif."
    total = float(row["R&D Spend"]) + float(row["Administration"]) + float(row["Marketing Spend"])
    if total == 0:
            return "total pengeluaran nol, efisiensi tidak dapat dihitung."
    return ""
def klasifikasi_efisiensi(efisiensi):
    if efisiensi >= BATAS_TINGGI:
        return "Tinggi"
    elif efisiensi >= BATAS_SEDANG:
        return "Sedang"
    else:
        return "Rendah"
def urutkan_efisiensi(data):
    data_urut = []
    for row in data:
        data_urut.append(row)
    for i in range(len(data_urut)):
        for j in range(len(data_urut) - 1 - i):
            if data_urut[j]["efisiensi"] < data_urut[j + 1]["efisiensi"]:
                sementara = data_urut[j]
                data_urut[j] = data_urut[j + 1]
                data_urut[j + 1] = sementara
    return data_urut
def hitung_rekap_state(data):
    rekap = {}
    for row in data:
        if row["state"] not in rekap:
            rekap[row["state"]] = {"jumlah": 0, "rnd": 0, "admin": 0, "marketing": 0, "total": 0,
                                   "profit": 0, "efisiensi": 0, "Tinggi": 0, "Sedang": 0, "Rendah": 0}
        r = rekap[row["state"]]
        r["jumlah"] += 1
        r["rnd"] += row["rnd"]
        r["admin"] += row["admin"]
        r["marketing"] += row["marketing"]
        r["total"] += row["total"]
        r["profit"] += row["profit"]
        r["efisiensi"] += row["efisiensi"]
        r[row["kategori"]] += 1
    return rekap
def tampilkan_ranking(data_urut):
    print("\nRANKING EFISIENSI STARTUP (Efisiensi = Profit / Total Pengeluaran)")
    print("=" * 116)
    print(f"| {'No':>3} | {'ID':<3} | {'State':<10} | {'R&D':>10} | {'Admin':>10} | {'Marketing':>10} "
          f"| {'Total Keluar':>12} | {'Profit':>10} | {'Efisiensi':>9} | {'Kategori':<8} |")
    print("=" * 116)
    for row in data_urut:
        print(f"| {row['peringkat']:>3} | {row['id']:<3} | {row['state']:<10} | {row['rnd']:>10,.2f} "
              f"| {row['admin']:>10,.2f} | {row['marketing']:>10,.2f} | {row['total']:>12,.2f} "
              f"| {row['profit']:>10,.2f} | {row['efisiensi']:>9.3f} | {row['kategori']:<8} |")
    print("=" * 116)
    print(f"Kriteria: Tinggi bila efisiensi >= {BATAS_TINGGI}, Sedang bila >= {BATAS_SEDANG}, selain itu Rendah")
    def tampilkan_rekap_state(rekap_state):
    print("\nREKAP RATA-RATA PER STATE")
    print("=" * 113)
    print(f"| {'State':<10} | {'Jumlah':>6} | {'Rata R&D':>10} | {'Rata Admin':>10} | {'Rata Mkt':>10} "
          f"| {'Rata Total':>10} | {'Rata Profit':>11} | {'Rata Efis.':>10} | {'T/S/R':>8} |")
    print("=" * 113)
    for state in rekap_state:
        r = rekap_state[state]
        n = r["jumlah"]
        tsr = f"{r['Tinggi']}/{r['Sedang']}/{r['Rendah']}"
        print(f"| {state:<10} | {n:>6} | {r['rnd'] / n:>10,.2f} | {r['admin'] / n:>10,.2f} "
              f"| {r['marketing'] / n:>10,.2f} | {r['total'] / n:>10,.2f} | {r['profit'] / n:>11,.2f} "
              f"| {r['efisiensi'] / n:>10.3f} | {tsr:>8} |")
    print("=" * 113)
    print("T/S/R = jumlah startup berkategori Tinggi / Sedang / Rendah")
    def tampilkan_ringkasan(data, data_tidak_valid):
    jumlah_tinggi = jumlah_sedang = jumlah_rendah = 0
    total_pengeluaran_semua = 0
    total_profit_semua = 0
    total_efisiensi = 0
    for row in data:
        if row["kategori"] == "Tinggi":
            jumlah_tinggi += 1
        elif row["kategori"] == "Sedang":
            jumlah_sedang += 1
        else:
            jumlah_rendah += 1
        total_pengeluaran_semua += row["total"]
        total_profit_semua += row["profit"]
        total_efisiensi += row["efisiensi"]
