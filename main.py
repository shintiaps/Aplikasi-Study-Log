catatan = []

def tambah_catatan():
    print("\n=== Tambah Catatan Belajar ===")
    mapel = input("Masukkan nama mata pelajaran: ").strip()
    if not mapel:
        print("Mapel tidak boleh kosong. Batal.")
        return
    topik = input("Masukkan topik yang dipelajari: ").strip()
    if not topik:
        print("Topik tidak boleh kosong. Batal.")
        return

    # Validasi durasi agar berupa angka bulat positif
    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        if not durasi_input:
            print("Durasi tidak boleh kosong.")
            continue
        if not durasi_input.isdigit():
            print("Masukkan angka bulat untuk durasi (dalam menit).")
            continue
        durasi = int(durasi_input)
        if durasi <= 0:
            print("Durasi harus lebih dari 0.")
            continue
        break

    # Gunakan dict sederhana agar mudah dipahami pemula
    catatan_entry = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }

    catatan.append(catatan_entry)
    print(f"✅ Catatan untuk '{mapel}' ({topik}, {durasi} menit) berhasil ditambahkan.")

def lihat_catatan():
    print("\n=== Daftar Catatan Belajar ===")
    if not catatan:
        print("Belum ada catatan. Silakan tambah catatan terlebih dahulu.")
        return

    for i, entry in enumerate(catatan, start=1):
        mapel = entry.get("mapel", "-")
        topik = entry.get("topik", "-")
        durasi = entry.get("durasi", "-")
        print(f"{i}. {mapel} - {topik} ({durasi} menit)")

    print(f"\nTotal catatan: {len(catatan)}")

def total_waktu():
    print("\n=== Total Waktu Belajar ===")
    if not catatan:
        print("Belum ada catatan. Silakan tambah catatan terlebih dahulu.")
        return

    total = sum(entry.get("durasi", 0) for entry in catatan)

    # Tampilkan dalam menit dan juga format jam+menit jika lebih dari 60 menit
    if total >= 60:
        jam = total // 60
        menit = total % 60
        print(f"Total waktu belajar: {total} menit ({jam} jam {menit} menit)")
    else:
        print(f"Total waktu belajar: {total} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
