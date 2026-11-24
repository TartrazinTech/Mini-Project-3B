import csv
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
