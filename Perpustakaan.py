from librarypuluh import filter_data, hitung_total, cari_item, kelompokkan_data, urutkan_data, cek_keberadaan

katalog_buku = [
    {"id": 1, "judul": "Pemrograman Fungsional dengan Python", "kategori": "Teknologi", "status": "Tersedia", "denda_harian": 2000},
    {"id": 2, "judul": "Baboning Pepak Basa Jawa", "kategori": "Bahasa", "status": "Dipinjam", "denda_harian": 1000},
    {"id": 3, "judul": "Struktur Data & Algoritma", "kategori": "Teknologi", "status": "Tersedia", "denda_harian": 2000},
    {"id": 4, "judul": "Kalkulus Lanjut", "kategori": "Sains", "status": "Dipinjam", "denda_harian": 1500}
]

def main():
    print("=== PROGRAM PERPUSTAKAAN MINI (FP) ===")

    # 1. Menggunakan filter_data
    print("\n[1] Buku yang Tersedia:")
    buku_ada = filter_data(katalog_buku, lambda x: x["status"] == "Tersedia")
    list(map(lambda b: print(f"- {b['judul']} ({b['kategori']})"), buku_ada))

    # 2. Menggunakan cek_keberadaan
    ada_jawa = cek_keberadaan(katalog_buku, "kategori", "Bahasa")
    print(f"\n[2] Cek Kategori 'Bahasa' di Katalog: {'Ada' if ada_jawa else 'Tidak ada'}")

    # 3. Menggunakan kelompokkan_data
    print("\n[3] Kelompok Buku Berdasarkan Kategori:")
    grup_kat = kelompokkan_data(katalog_buku, "kategori")
    for kat, daftar in grup_kat.items():
        print(f"-> {kat}: {len(daftar)} buku")

    # 4. Menggunakan urutkan_data
    print("\n[4] Urutan Buku Berdasarkan Denda Tertinggi:")
    buku_urut = urutkan_data(katalog_buku, "denda_harian", reverse=True)
    list(map(lambda b: print(f"- {b['judul']} (Rp {b['denda_harian']})"), buku_urut))

    # 5. Menggunakan hitung_total (reduce)
    total_denda = hitung_total(katalog_buku, "denda_harian")
    print(f"\n[5] Akumulasi Total Denda Harian: Rp {total_denda}")

if __name__ == "__main__":
    main()