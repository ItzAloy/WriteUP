import string

def rot18(teks):
    # Tabel translasi untuk huruf dengan ROT13
    rot13_table = str.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    )
    # Tabel translasi untuk digit dengan ROT5
    rot5_table = str.maketrans("0123456789", "5678901234")
    
    # Terapkan ROT13 untuk huruf
    hasil = teks.translate(rot13_table)
    # Terapkan ROT5 untuk digit
    hasil = hasil.translate(rot5_table)
    return hasil

# Contoh penggunaan
pesan_asli = """Lorem Ipsum"""
cipher = rot18(pesan_asli)
plain = rot18(cipher)  # Penerapan kedua mengembalikan pesan asli

print("Pesan Asli    :", pesan_asli)
print("Cipher Text   :", cipher)