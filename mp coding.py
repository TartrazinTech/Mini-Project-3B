import csv
file_csv=r"50_Startups.csv"
Kolom_Wajib=["R&D Spend", "Administration", "Marketing Spend", "State", "Profit"]
Kolom_Teks=["State"]
Kolom_Angka=["R&D Spend", "Administration", "Marketing Spend", "Profit"]
def buka_file(file_csv, kolom_wajib):
    