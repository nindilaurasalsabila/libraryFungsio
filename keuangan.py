from librarypuluh import filter_data, hitung_total, kelompokkan_data, cari_item, ambil_unik, cek_keberadaan

riwayat_transaksi = [
    {"id": 1, "deskripsi": "Gaji Freelance", "jenis": "Pemasukan", "jumlah": 1500000, "kategori": "Pekerjaan"},
    {"id": 2, "deskripsi": "Makan Mie Gacoan", "jenis": "Pengeluaran", "jumlah": 25000, "kategori": "Makanan"},
    {"id": 3, "deskripsi": "Beli Teh Kota", "jenis": "Pengeluaran", "jumlah": 12000, "kategori": "Minuman"},
    {"id": 4, "deskripsi": "Top-up BRImo", "jenis": "Pengeluaran", "jumlah": 50000, "kategori": "Transport"},
    {"id": 5, "deskripsi": "Joki Coding Temen", "jenis": "Pemasukan", "jumlah": 100000, "kategori": "Pekerjaan"}
]

def main():
    print("=== PROGRAM KEUANGAN PRIBADI (FP) ===")

    # 1. Menggunakan filter_data
    print("\n[1] Riwayat Pengeluaran:")
    pengeluaran = filter_data(riwayat_transaksi, lambda x: x["jenis"] == "Pengeluaran")
    list(map(lambda p: print(f"- {p['deskripsi']} : Rp {p['jumlah']}"), pengeluaran))

    # 2. Menggunakan cek_keberadaan
    ada_gaji = cek_keberadaan(riwayat_transaksi, "deskripsi", "Gaji Freelance")
    print(f"\n[2] Cek Transaksi 'Gaji Freelance': {'Ada' if ada_gaji else 'Tidak ada'}")

    # 3. Menggunakan hitung_total (reduce)
    total_keluar = hitung_total(pengeluaran, "jumlah")
    print(f"\n[3] Total Pengeluaran: Rp {total_keluar}")

    # 4. Menggunakan kelompokkan_data
    print("\n[4] Pengelompokan Berdasarkan Jenis:")
    grup_jenis = kelompokkan_data(riwayat_transaksi, "jenis")
    for jenis, items in grup_jenis.items():
        print(f"-> {jenis}: {len(items)} transaksi")

    # 5. Menggunakan ambil_unik
    kategori_unik = ambil_unik(riwayat_transaksi, "kategori")
    print(f"\n[5] Kategori Transaksi Unik: {kategori_unik}")

if __name__ == "__main__":
    main()