def caesar_encrypt(teks, pergeseran):
    hasil = ""
    for char in teks:
        if char.isalpha():
            basis = 65 if char.isupper() else 97
            hasil += chr((ord(char) - basis + pergeseran) % 26 + basis)
        else:
            hasil += char
    return hasil

def caesar_decrypt(teks, pergeseran):
    return caesar_encrypt(teks, -pergeseran)

# Contoh penggunaan
pesan_asli = """controh"""
pergeseran = 13
cipher = caesar_encrypt(pesan_asli, pergeseran)
plain = caesar_decrypt(cipher, pergeseran)

print("Pesan Asli    :", pesan_asli)
print("Cipher Text   :", cipher)
print("Dekripsi Hasil:", plain)