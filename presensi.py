from librarypuluh import filter_data, hitung_frekuensi, cari_item, transform_data, cek_keberadaan

data_presensi = [
    {"id": 1, "nama": "Nindi Laura Salsabila", "nim": "202410370110300", "status": "Hadir"},
    {"id": 2, "nama": "Anin", "nim": "202410370110301", "status": "Hadir"},
    {"id": 3, "nama": "Shofwan Alif", "nim": "202410370110302", "status": "Hadir"},
    {"id": 4, "nama": "Nabiila", "nim": "202410370110303", "status": "Izin"},
    {"id": 5, "nama": "Karina", "nim": "202410370110304", "status": "Hadir"},
    {"id": 6, "nama": "Ell", "nim": "202410370110305", "status": "Alfa"}
]

def main():
    print("=== PROGRAM PRESENSI KELAS (FP) ===")

    # 1. Menggunakan filter_data
    print("\n[1] Daftar Mahasiswa Hadir:")
    mhs_hadir = filter_data(data_presensi, lambda x: x["status"] == "Hadir")
    list(map(lambda m: print(f"- {m['nama']} ({m['nim']})"), mhs_hadir))

    # 2. Menggunakan cek_keberadaan
    ada_anin = cek_keberadaan(data_presensi, "nama", "Anin")
    print(f"\n[2] Cek Keberadaan Anin di Absen: {'Ada' if ada_anin else 'Tidak ada'}")

    # 3. Menggunakan transform_data (map) untuk format teks baru
    print("\n[3] Format Keterangan Singkat:")
    ringkasan = transform_data(data_presensi, lambda m: f">> {m['nama']} [{m['status']}]")
    list(map(print, ringkasan))

    # 4. Menggunakan hitung_frekuensi (reduce)
    print("\n[4] Statistik Status Kehadiran:")
    statistik = hitung_frekuensi(data_presensi, "status")
    for status, jumlah in statistik.items():
        print(f"-> {status}: {jumlah} orang")

    # 5. Menggunakan cari_item
    cari_id = 2
    hasil = cari_item(data_presensi, "id", cari_id)
    print(f"\n[5] Pencarian ID {cari_id}: {hasil['nama'] if hasil else 'Tidak ada'}")

if __name__ == "__main__":
    main()