from librarypuluh import filter_data, hitung_rata_rata, urutkan_data, cari_item, ambil_top_n, cek_keberadaan

data_nilai = [
    {"id": 1, "nama": "Nindi Laura Salsabila", "nim": "202410370110300", "nilai_akhir": 88.5, "grade": "A"},
    {"id": 2, "nama": "Anin", "nim": "202410370110301", "nilai_akhir": 85.0, "grade": "A"},
    {"id": 3, "nama": "Shofwan Alif", "nim": "202410370110302", "nilai_akhir": 78.0, "grade": "B"},
    {"id": 4, "nama": "Nabiila", "nim": "202410370110303", "nilai_akhir": 90.5, "grade": "A"},
    {"id": 5, "nama": "Karina", "nim": "202410370110304", "nilai_akhir": 72.5, "grade": "B"},
    {"id": 6, "nama": "Ell", "nim": "202410370110305", "nilai_akhir": 65.0, "grade": "C"}
]

def main():
    print("=== PROGRAM NILAI MAHASISWA (FP) ===")

    # 1. Menggunakan filter_data
    print("\n[1] Mahasiswa dengan Grade 'A':")
    grade_a = filter_data(data_nilai, lambda x: x["grade"] == "A")
    list(map(lambda m: print(f"- {m['nama']} ({m['nilai_akhir']})"), grade_a))

    # 2. Menggunakan cek_keberadaan
    ada_anin = cek_keberadaan(data_nilai, "nama", "Anin")
    print(f"\n[2] Cek Data Nilai 'Anin': {'Ada' if ada_anin else 'Tidak ada'}")

    # 3. Menggunakan hitung_rata_rata
    rata = hitung_rata_rata(data_nilai, "nilai_akhir")
    print(f"\n[3] Rata-rata Nilai Kelas: {rata:.2f}")

    # 4. Menggunakan ambil_top_n
    print("\n[4] Top 3 Nilai Tertinggi:")
    top_tiga = ambil_top_n(data_nilai, "nilai_akhir", 3)
    list(map(lambda m: print(f"- {m['nama']} : {m['nilai_akhir']}"), top_tiga))

    # 5. Menggunakan urutkan_data
    print("\n[5] Urutan Nilai dari Terendah:")
    urut_naik = urutkan_data(data_nilai, "nilai_akhir", reverse=False)
    list(map(lambda m: print(f"- {m['nama']} : {m['nilai_akhir']}"), urut_naik))

if __name__ == "__main__":
    main()