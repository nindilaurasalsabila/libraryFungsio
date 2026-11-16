from librarypuluh import filter_data, transform_data, hitung_total, cari_item, urutkan_data, cek_keberadaan

menu_kantin = [
    {"id": 1, "nama": "Mie Gacoan Level 1", "kategori": "Makanan", "harga": 10000},
    {"id": 2, "nama": "Udang Rambutan", "kategori": "Cemilan", "harga": 9000},
    {"id": 3, "nama": "Siomay Ayam", "kategori": "Cemilan", "harga": 9500},
    {"id": 4, "nama": "Teh Kotak", "kategori": "Minuman", "harga": 5000},
    {"id": 5, "nama": "Es Teh Manis", "kategori": "Minuman", "harga": 3000}
]

def main():
    print("=== PROGRAM KASIR KANTIN (FP) ===")
    
    # 1. Menggunakan filter_data & transform_data (map)
    print("\n[1] Daftar Menu Makanan:")
    makanan = filter_data(menu_kantin, lambda x: x["kategori"] == "Makanan")
    list(map(lambda m: print(f"- {m['nama']} (Rp {m['harga']})"), makanan))

    # 2. Menggunakan cek_keberadaan
    ada_menu = cek_keberadaan(menu_kantin, "nama", "Es Teh Manis")
    print(f"\n[2] Cek Menu 'Es Teh Manis': {'Tersedia' if ada_menu else 'Tidak ada'}")

    # 3. Menggunakan urutkan_data
    print("\n[3] Menu Urut Harga Termurah:")
    menu_termurah = urutkan_data(menu_kantin, "harga", reverse=False)
    list(map(lambda m: print(f"- {m['nama']} : Rp {m['harga']}"), menu_termurah))

    # 4. Simulasi keranjang & hitung_total (reduce)
    keranjang = [
        {"id": 1, "nama": "Mie Gacoan Level 1", "harga": 10000, "qty": 2},
        {"id": 5, "nama": "Es Teh Manis", "harga": 3000, "qty": 3}
    ]
    keranjang_sub = transform_data(keranjang, lambda item: {**item, "subtotal": item["harga"] * item["qty"]})
    total = hitung_total(keranjang_sub, "subtotal")
    print(f"\n[4] Total Belanja: Rp {total}")

if __name__ == "__main__":
    main()