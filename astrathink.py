import json
import os

DATA_FILE = "kas_kelas.json"

# ------------------------------
# Fungsi untuk memuat data
# ------------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"siswa": {}, "total": 0}

# ------------------------------
# Fungsi untuk menyimpan data
# ------------------------------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Data berhasil disimpan!\n")

# ------------------------------
# Tambah siswa baru
# ------------------------------
def tambah_siswa(data):
    nama = input("Masukkan nama siswa baru: ")
    if nama in data["siswa"]:
        print("Siswa sudah terdaftar!\n")
    else:
        data["siswa"][nama] = 0
        print(f"Siswa '{nama}' berhasil ditambahkan!\n")

# ------------------------------
# Bayar kas
# ------------------------------
def bayar_kas(data):
    nama = input("Nama siswa yang membayar: ")

    if nama not in data["siswa"]:
        print("Nama tidak ditemukan! Tambah siswa dulu.\n")
        return

    jumlah = int(input("Jumlah pembayaran: Rp "))
    data["siswa"][nama] += jumlah
    data["total"] += jumlah

    print(f"{nama} membayar Rp {jumlah}. Pembayaran berhasil!\n")

# ------------------------------
# Lihat saldo & laporan 
# ------------------------------
def lihat_saldo(data):
    print("\n=== LAPORAN KAS KELAS ===")
    for nama, bayar in data["siswa"].items():
        print(f"- {nama} : Rp {bayar}")
    print(f"\nTOTAL KAS: Rp {data['total']}\n")

# ------------------------------
# Menu utama
# ------------------------------
def menu():
    data = load_data()

    while True:
        print("=== MENU UANG KAS KELAS ===")
        print("1. Tambah Siswa")
        print("2. Bayar Kas")
        print("3. Lihat Saldo Kas")
        print("4. Simpan ke File")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa(data)
        elif pilihan == "2":
            bayar_kas(data)
        elif pilihan == "3":
            lihat_saldo(data)
        elif pilihan == "4":
            save_data(data)
        elif pilihan == "5":
            save_data(data)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")

# ------------------------------
# Jalankan program
# ------------------------------
menu()