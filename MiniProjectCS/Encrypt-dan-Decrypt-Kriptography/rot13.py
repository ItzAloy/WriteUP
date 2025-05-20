import string

def rot13(teks):
    tabel_trans = str.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    )
    return teks.translate(tabel_trans)

# Contoh penggunaan
pesan_asli = """Lorem Ipsum"""
cipher = rot13(pesan_asli)
plain = rot13(cipher)  # Penerapan kedua mengembalikan pesan asli

print("Pesan Asli   :", pesan_asli)
print("Cipher Text  :", cipher)
