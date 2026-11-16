from functools import reduce

def filter_data(data, predikat):
    """Menyaring elemen berdasarkan kondisi fungsional (filter)."""
    return list(filter(predikat, data))

def transform_data(data, fungsi):
    """Mengubah/memetakan data (map) menjadi format baru."""
    return list(map(fungsi, data))

def hitung_total(data, key):
    """Menjumlahkan nilai dari kunci tertentu dalam daftar data (reduce)."""
    return reduce(lambda acc, item: acc + item.get(key, 0), data, 0)

def hitung_rata_rata(data, key):
    """Menghitung rata-rata dari atribut numerik."""
    if not data:
        return 0.0
    return hitung_total(data, key) / len(data)

def cari_item(data, key, value):
    """Mencari elemen pertama yang cocok (search)."""
    return next((item for item in data if item.get(key) == value), None)

def hitung_frekuensi(data, key):
    """Menhitung jumlah kemunculan nilai tertentu."""
    def akumulasi(acc, item):
        val = item.get(key)
        acc[val] = acc.get(val, 0) + 1
        return acc
    return reduce(akumulasi, data, {})

def urutkan_data(data, key, reverse=False):
    """Mengurutkan daftar data berdasarkan kunci tertentu."""
    return sorted(data, key=lambda x: x.get(key, 0), reverse=reverse)

def cek_keberadaan(data, key, value):
    """Memeriksa apakah suatu nilai ada dalam data (any/exists)."""
    return any(item.get(key) == value for item in data)

def ambil_top_n(data, key, n=3):
    """Mengambil n data tertinggi atau teratas."""
    return urutkan_data(data, key, reverse=True)[:n]

def kelompokkan_data(data, key):
    """Mengelompokkan data berdasarkan kategori/status."""
    def akumulasi(acc, item):
        kategori = item.get(key)
        acc.setdefault(kategori, []).append(item)
        return acc
    return reduce(akumulasi, data, {})


def cari_banyak(data, key, value):
    """Mencari semua elemen yang cocok dengan nilai tertentu."""
    return [item for item in data if item.get(key) == value]

def ambil_unik(data, key):
    """Mengambil daftar nilai unik dari suatu kunci/atribut."""
    return list(set(item.get(key) for item in data if key in item))

def gabung_data(data1, data2, key1, key2):
    """Menggabungkan dua daftar data berdasarkan kecocokan kunci (Join)."""
    hasil = []
    for item1 in data1:
        match = next((item2 for item2 in data2 if item2.get(key2) == item1.get(key1)), None)
        if match:
            hasil.append({**item1, **match})
    return hasil